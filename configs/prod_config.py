from configs.config import Config


class ProductionConfig(Config):
    DB_NAME = "dynamodb"
    SNS = "sns"
    AWS_ACCESS_KEY_ID = "ASIAWOYNGN4BHI6IYP47"
    AWS_SECRET_ACCESS_KEY = "ADhNE8pKJMJ0zL3VPOHCaGw1ooMCZMcsIgFa2Fee"
    AWS_SESSION_TOKEN = "FwoGZXIvYXdzEBAaDBhMkdbmVtynFm+EUyLAATx+Z+wKy9T8JnaYWhMkPPB6lOrT6cbfUYBo2KDekWdYI/HrQEnuAl+2Sj0fgv48L2sl/lH7Jbb7RU+kIZeFERM6WWIrBO1ApFCPUVdCluXLj5ivJ62EYmVIs2lctvtjD3SGEw6/FXpOUStmmN0+4ZPkEHVsTLwmnnkpvxYN2Onug9zP90YzyYUVy2YMvRipckfmtu5NksR07zVcLeUbDZbAmewfI9U8WDwvG2FwgJPVgQwkjvX3Ja0zR9+aaExqKij7i7OSBjItyjEVpQOWr5XBIQlITzyMzxC1DU5iQ1OU7GTdkNIZ2kQAJBeiJMo6uKj2tE2e"
    AWS_REGION = "us-east-1"
    AWS_SESSION = ""
    BUCKET_NAME = "servicerequestimage"
    COGNITO_CLIENT_ID = "2g2bbfsshtrt34fsp15sacir1r"
    AUTH_FLOW = "USER_PASSWORD_AUTH"

