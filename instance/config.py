import os

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv( 'SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv( 'DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    }
    
