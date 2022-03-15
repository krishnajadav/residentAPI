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
        service_request = ServiceRequest()
        data = service_request.get_all_requests()
        return {"response_data":data},200
    except Exception as e:
        logging.log(e.args)
        return "Exception occurred", 500
    
    
@app.route("/post-service-request", methods=['POST'])
def store_service_request():
    json_data = request.json
    request_id = json_data["request_id"]
    request_category = json_data["request_category"],
    user_id = json_data["user_id"]
    request_title = json_data["request_title"]
    request_description = json_data["request_description"]
    request_image = json_data["request_image"]
    
    try:
        service_request = ServiceRequest()
        data = {
            "request_id": request_id,
            "user_id": user_id, 
            "request_category": request_category,
            "request_title": request_title,
            "request_description": request_description,
            "request_image": request_image
        }
        response = service_request.insert_service_request(data)
        return response, 200
    except Exception as e:
        logging.log(e.args)
        return "Exception occured", 500


if __name__ == "__main__":
    app.run(debug=True, port=5556)
