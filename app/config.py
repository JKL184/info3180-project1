import os

class Config(object):
    """Base Config Object"""
    DEBUG=False
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI='postgresql://vjpvpjsrhhdcbm:c31c0d0ab0fa0b55c54cdc7da16144dfa7913ba61ad5264abc49db58341762cd@ec2-54-161-239-198.compute-1.amazonaws.com:5432/dcunh5kvto19im'
    SQLALCHEMY_TRACK_MODIFICATIONS=False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER='./uploads/'
    

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False