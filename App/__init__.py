from flask import Flask
import os

from flask_login import LoginManager
login = LoginManager()

def create_app():
    from . import models, routes, services
    app = Flask(__name__)

    # grabs config data
    app.config.from_object('config.Config')

    login.init_app(app)
    login.login_view = 'login'
    
    models.init_app(app)
    routes.init_app(app)
    # services.init_app(app)
    

    
    #testing config
    print(f"Environment: {app.config['ENV']}")
    print(f"Debug: {app.config['DEBUG']}")
    print(f"IGDB api key: {app.config['IGDB_API_KEY']}")
    print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    return app