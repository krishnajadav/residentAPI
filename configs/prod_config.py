from configs.config import Config


class ProductionConfig(Config):
    DB_NAME = "dynamodb"
    SNS = "sns"
    AWS_ACCESS_KEY_ID = "ASIAWOYNGN4BLZ5PGUWO"
    AWS_SECRET_ACCESS_KEY = "HpZNgkn0J1QBy6WjOrWEwUpLgrk7GY+kXS3Wzfdp"
    AWS_SESSION_TOKEN = "FwoGZXIvYXdzEN3//////////wEaDBwFPnbm/dyGkCKFGyLAAdx73UMUQDFVxjY9nUyJVVaD3D/WV/PoSu6+vIiqUTT0uXAce7tpFUyEKhhUcI6d6605xg/2cMJEPEnmxBVOm4m2vSzRoIwETEdhGvCfcxsTnv4m0+BrC692ywYOOgLSaYLn7EyN1tI5J1fhTFj5T4d4X3rgC6Au4IL5SCneCbhI/NgCO7lOL+2VEn4hsA+IPKyQafNg5IKo0iJXqhouadt4w14gSrx90iSBNYrwgzvn9psbtPXZos5RbzlLp9cb3iiu4aeSBjItuoaw5g+/wDvDGuV0oGtk+f6iTB4kXDUFcMMsDPI7Ou4j05X3fLvLF6NysyEE"
    AWS_REGION = "us-east-1"
    AWS_SESSION = ""
    BUCKET_NAME = "servicerequestimage"
    COGNITO_CLIENT_ID = "2g2bbfsshtrt34fsp15sacir1r"
    AUTH_FLOW = "USER_PASSWORD_AUTH"

