from configs.config import Config


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "dynamodb"
    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    AWS_SESSION_TOKEN = ""
    AWS_REGION = ""
