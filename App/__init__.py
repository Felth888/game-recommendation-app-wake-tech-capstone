from flask import Flask
import os

def create_app():
    from . import models, routes, services
    app = Flask(__name__)
    # models.init_app(app)
    routes.init_app(app)
    # services.init_app(app)

    # grabs config data
    app.config.from_object('config.Config')
    #testing config
    print(f"Environment: {app.config['ENV']}")
    print(f"Debug: {app.config['DEBUG']}")
    print(f"IGDB api key: {app.config['IGDB_API_KEY']}")
    
    
    return app