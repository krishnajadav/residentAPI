import boto3
from flask import Flask, request, json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userInfo')

app = Flask(__name__)
if app.config("ENV") == "production":
    app.config.from_object("configs.dev_config.ProductionConfig")
else:
    app.config.from_object("configs.dev_config.DevelopmentConfig")  # add config values in configs folder and
    # retrieve anywhere in the project using app.config("key")


@app.route("/user/authentication", methods=['POST', 'GET'])
def index():
    json_input = json.loads(json.dumps(request.json))
    response = table.scan(
        FilterExpression=Key('user_Name').eq(json_input['userName']) & Key('user_Password').eq(json_input['password'])
    )

    if len(response['Items']) == 1:
        return "Authenticate successfully"
    else:
        return "Invalid UserName and Password"


if __name__ == "__main__":
    app.run(debug=True, port=5555)
