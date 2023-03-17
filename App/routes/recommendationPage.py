from flask import Blueprint, render_template, request, current_app, json
from flask_login import current_user, login_required
from sqlalchemy import sql
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import requests

from ..services.libraryUtils import getLibraryString, getWishlistString

bp = Blueprint('recommendationPage', __name__)

from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from ..models import db

@bp.route('/recommendationpage', methods=['GET', 'POST'])
@login_required
def recommendationPage():
    lib_id_string = getLibraryString(current_user.id)
    wish_id_string = getWishlistString(current_user.id)
    return render_template('recommendation.html', title='Recommendations', library_id_list=lib_id_string, wishlist_id_list = wish_id_string)
    
@bp.route('/recommendCall', methods=['POST'])
def recommend():

    # Get current users game library & wishlist from database and input into dataframe.
    conn = db.engine.connect()
    user_games = pd.read_sql(sql = sql.text(f"""SELECT g.id, g.title, g.cover, g.genre, g.theme, g.play_mode, g.developer, g.release_date 
                                                FROM games as g 
                                                JOIN user_games as ug ON g.id = ug.game_id 
                                                WHERE ug.user_id = '{current_user.id}' 
                                                AND g.base_game
                                                AND NOT ug.archived 
                                                ORDER BY ug.id DESC;"""),
                                                con=conn)
    conn.close()
        
    # Make a POST request to get the data for the selection of games from IGDB
    url = "https://5jmkis1ked.execute-api.us-west-2.amazonaws.com/production/v4/games"

    payload = "fields name, cover.image_id, release_dates.date, genres.name, themes.name, game_modes.name, involved_companies.company.name, involved_companies.developer;"
    # get selections for each category indicating a base game and combine into a dataframe
    categories = [0, 3, 8, 9, 10]
    game_dfs = []
    for category in categories:
        payload += "where category =" + str(category) + "; limit 200;"
        headers = {"x-api-key": current_app.config['IGDB_API_KEY'], 'Content-Type': 'application/json'}

        post_response = requests.request("POST", url, data=payload, headers=headers)

        games = json.loads(post_response.text)
        game_selection = pd.json_normalize(games)
        
        game_dfs.append(game_selection)
    
    games = pd.concat(game_dfs)
    games.drop(['cover.id'], axis = 1, inplace=True)
    games.rename(columns={'name':'title','game_modes':'play_mode','involved_companies':'developer',
                          'genres':'genre','themes':'theme', 'release_dates':'release_date', 'cover.image_id':'cover'},
                            inplace=True)
    
    # extracts name values from metadata field dicts
    features = ['play_mode','genre','theme','developer','release_date']
    for feature in features:
        games[feature] = games[feature].apply(extract_data,args=([feature]))

    # create final game dataframe for finding recommendations
    # up to 5 games from library will be used to find recommendations
    if user_games.shape[0] > 5:
        # exludes games from library not included in selection from dataframe 
        unused_game_ids = user_games.id.tail(-5).values.tolist()
        games = games[~games.id.isin(unused_game_ids)]
                
        # remove unused games from user games dataframe
        user_games = user_games.head().copy()
   
    # add create list of selected titles and then combine dataframes
    selected_titles = user_games.title.values.tolist()
    games = pd.concat([games, user_games])
    games.drop_duplicates(subset=['id'], inplace=True)
    
    # combine metadata into soup field to use in similarity calculations
    # copy of dataframe created to preserve null values in original
    game_metadata = games[['id','genre','theme','play_mode','developer']].copy()
    
    features = ['genre','theme','play_mode','developer']
    for feature in features:
        game_metadata[feature].fillna('',inplace=True)
        game_metadata[feature] = game_metadata[feature].apply(clean_metadata)
    
    game_metadata['soup'] = game_metadata.apply(create_soup,axis=1)
    
    games = pd.merge(games,game_metadata[['id','soup']], on='id')
    
    # create count_matrix to calculate similarity between words
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(games['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # reset index to game title
    games = games.reset_index()
    indices = pd.Series(games.index, index=games['title'])

    # get game recommendations for each title selected from user library
    recommendations = []
    for title in selected_titles:
        # required to filter out titles from results
        filter_titles = selected_titles.remove(title)
        game_indices = get_recommendations(title, filter_titles, cosine_sim, indices)
        recommendations.append(games.iloc[game_indices].sample(n=5))
        
    game_recommendations = pd.concat(recommendations)
    game_recommendations.drop_duplicates(inplace=True)
    game_recommendations.drop(columns=['soup', 'index'], inplace=True)
    game_recommendations['base_game'] = True
    
    recommend_json = game_recommendations.to_json(orient='records')
    returnArr = json.loads(recommend_json)
    
    #getGame = Game.query.filter_by(id=request.form['id']).first()
#    returnArr = {
#        'id':getGame.id, 
#        'title':getGame.title,
#        'cover':getGame.cover,
#        'base_game':getGame.base_game,
#        'release_date':getGame.release_date,
#        'genre':getGame.genre,
#        'theme':getGame.theme,
#        'play_mode':getGame.play_mode,
#        'developer':getGame.developer
#    }

    return returnArr

def extract_data(x, feature):
    """extracts the values for game metadata fields

        name values are formatted and added to list which is converted to string
        date value is converted to datetime and returned
    """
    # verifies that the field contains a value, eliminates need for try and except.
    if isinstance(x, list):
        names = []
        # involved_companies have additional levels to reach developer names
        if feature != 'developer' and feature != 'release_date':
            for id in x:
                names.append(str.lower(id['name']))
        elif feature == 'developer':
            for company in x:
                # required to exclude publisher names
                if company['developer']:
                    names.append(str.lower(company['company']['name']))
        else:
            # no release date shows as empty lists so try and except necessary
            try:    
                mS = int(x[0]['date'])
                release_date = datetime.utcfromtimestamp(mS).strftime('%Y-%m-%d')
                return release_date
            except Exception as e:
                return None
            
        names = ','.join(names)
        return names
    else:
        return x

def clean_metadata(x):
    """strips spaces and then replaces commas with spaces"""
    if isinstance(x, str):
        x = x.replace(' ','')
        return x.replace(',',' ')

def create_soup(x):
    """combine all metadata into single string"""
    return x['genre'] + ' ' + x['theme'] + ' ' + x['play_mode'] + ' '+ x['developer']


def get_recommendations(title, filter_titles, cosine_sim, indices):
    """finds 5 recommendations for a game title
    
       calculates similarity score between all games and
       selects 5 random titles from top 20"""
    
    idx = indices[title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:21]
    
    return [i[0] for i in sim_scores] 