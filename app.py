import boto3
from flask import Flask, request, json
from boto3.dynamodb.conditions import Key
from entities.service_request import ServiceRequest
import logging

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("configs.prod_config.ProductionConfig")
else:
    app.config.from_object("configs.dev_config.DevelopmentConfig")  # add config values in configs folder and
    # retrieve anywhere in the project using app.config("key")

@app.route("/")
def init_test():
    return "<h2>Welcome to Resident Service Portal.</h2><h3>Application is running.</h3>"

@app.route("/users/authentication", methods=['POST', 'GET'])
def index():
    json_input = json.loads(json.dumps(request.json))
    dynamodb = boto3.resource(app.config["DB_NAME"])
    table = dynamodb.Table('t_User_Info')
    response = table.scan(
        FilterExpression=Key('User_Name').eq(json_input['userName']) & Key('User_Password').eq(json_input['password'])
    )

    if len(response['Items']) == 1:
        return "Authenticate successfully"
    else:
        return "Invalid UserName and Password"


@app.route("/service-requests", methods=['GET'])
def get_all_service_requests():
    try:
        data = ServiceRequest.get_all_requests()
        return data, 200
    except Exception as e:
        logging.log(e.args)
        return "Exception occurred", 500


if __name__ == "__main__":
    app.run(debug=True, port=5555)
