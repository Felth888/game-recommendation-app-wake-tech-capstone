import os
basedir = os.path.abspath(os.path.dirname(__file__))

# add any environmental secrets, aka igdb secrets to this class
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IGDB_API_KEY = 
    JWT_SECRET = 
    MAIL_SERVER = 
    MAIL_PORT = 
    MAIL_USE_SSL = True
    MAIL_USERNAME = 
    MAIL_PASSWORD = 

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True