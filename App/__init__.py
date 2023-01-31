from flask import Flask

def create_app():
    from . import models, routes, services
    app = Flask(__name__)
    # models.init_app(app)
    routes.init_app(app)
    # services.init_app(app)
    return app