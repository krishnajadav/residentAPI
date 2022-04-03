from configs.config import Config


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "dynamodb"
    SNS = "sns"
    AWS_ACCESS_KEY_ID = "ASIAWOYNGN4BNUUG2XMM"
    AWS_SECRET_ACCESS_KEY = "vEjPXnR4hTPxI0ISqQAPJnHyLDb/o/DBp6ububY0"
    AWS_SESSION_TOKEN = "FwoGZXIvYXdzEMf//////////wEaDJRsLCbjR6BFVJc4yCLAAQC/xUVBAkNiXPoZZgLRCybUzfyzWHK7IOHCNKg3k5vI12lYVmfWNMIwGx4Nz24MjjeLuQUidtkja3JY85dI0vFWfoK7VvCdlZ/goF3UHYeKGXvKKj2Ct1xby3leBkRH9oyvXFYBHApwBRouf9OxTfbuu+zJE4L7qHV1MeqGvvcFoOKtKy9ac4P0ZyoGxHyo2SYStq7GDaWvu6CWLilKua/4XuQ4fOTEnBG9VhzKVzRN9AKQJyaS2pyPB/03GXBblyiwjqOSBjItQhxUOGOlD7sjpH5kQZgT2C9JuyMs04dR5bDwAi6lNUVsqe/gUmSecQQjdhOm"
    AWS_REGION = "us-east-1"
    AWS_SESSION = ""
