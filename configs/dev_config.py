from configs.config import Config


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "dynamodb"
    SNS = "sns"
    AWS_ACCESS_KEY_ID = "ASIAWOYNGN4BPIGYDI6G"
    AWS_SECRET_ACCESS_KEY = "mZiYgZbpiGwJiO4RAGmcsQG2hAF+WHia5+F+TLjR"
    AWS_SESSION_TOKEN = "FwoGZXIvYXdzENb//////////wEaDH626DSVpTpBlAaUIyLAAUls1KnewaveDZ9uVxxTpaqP3sbVEhZJOLnRnxJioqwna7Kt+2nlYIoCAcajVlCVDZHRzfMX5iO0kZkruKEI8jsLCZ19gyu1ktZp34ivupQEM0PwgOPk8/fkYxodffSzfT5yGjoKLrhtZ9GJnoq49UqGZXOOCZIib2Nt92sk/8Dxy0wZ1otdUPgdpS5xqZdBWrJbxJTVoO0nsVpOdpE4FCqGoI+lb8cmP/hDrKq40FkSM9ZEZi+zApHns/Pu+Rh7gyjXnaaSBjItxCU7NVjLITPcFKfBkJJBL92ELTsiOLO1UUgRZTn/YaFt5i7Qsou/MZI6NaqJ"
    AWS_REGION = "us-east-1"
    AWS_SESSION = ""
    BUCKET_NAME = "servicerequestimage"
