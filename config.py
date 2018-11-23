class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = "sqlite:////tmp/chapu.db"


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = "sqlite:////tmp/chapu_test.db"


configs = {
    'dev': DevelopmentConfig,
    'test': TestingConfig
}