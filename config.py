
class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
