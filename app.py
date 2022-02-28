import boto3
from flask import Flask, request, json,jsonify
from boto3.dynamodb.conditions import Key
from flask_cors import CORS

client = boto3.client('cognito-idp')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userInfo')

app=Flask(__name__)
CORS(app)
if app.config("ENV") == "production":
    app.config.from_object("configs.dev_config.ProductionConfig")
else:
    app.config.from_object("configs.dev_config.DevelopmentConfig")  # add config values in configs folder and
    # retrieve anywhere in the project using app.config("key")


@app.route("/user/authentication",methods=['POST','GET'])
def index():
    jsonInput = request.get_json()
    userName=jsonInput['userName']
    password=jsonInput['password']
    adminResult=checkAdminUser(userName,password)
    if adminResult!="Admin":
        response = table.scan(
            FilterExpression=Key('user_Name').eq(userName) & Key('user_Password').eq(password)
        )
        if len(response['Items'])==1:
            return jsonify(success=True, data="Resident Authenticate successfully")
        else:
            return jsonify(success=False, data="Invalid UserName and Password")
    else:
        return jsonify(success=True, data="Administrator Authenticate successfully")

def checkAdminUser(username, password):
    try:
      CognitoResponse = client.initiate_auth(
            ClientId="2g2bbfsshtrt34fsp15sacir1r",
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME':username,
                'PASSWORD':password,
            })
    except client.exceptions.NotAuthorizedException:
        return None
    except client.exceptions.UserNotConfirmedException:
        return None
    except Exception as e:
        return None
    return "Admin"

if __name__ == "__main__":
    app.run(debug=True, port=5555)
