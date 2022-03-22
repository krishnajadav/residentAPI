import uuid
from crypt import methods
import boto3
from flask import Flask, request, json
from boto3.dynamodb.conditions import Key
from entities.service_request import ServiceRequest
from entities.sns_operation import SNSOperation

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

        sns = SNSOperation()
        sns.publish_notification("GET Requested", "By Admin")

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
            "request_id": uuid.uuid4(),
            "user_id": user_id,
            "request_category": request_category,
            "request_title": request_title,
            "request_description": request_description,
            "request_image": request_image
        }
        response = service_request.insert_service_request(data)

        sns = SNSOperation()
        sns.publish_notification(f"Hi! You have a new service request: \n Request ID: {request_id} \n Request Title: {request_title}", f"New Service Request from {user_id}")

        return response, 200

    except Exception as e:
        logging.log(e.args)
        return "Exception occured", 500
    

@app.route("/delete-request/<int:id>", methods=['DELETE'])
def delete_request(id):
    service_request = ServiceRequest()
    response = service_request.delete_service_request(id);
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):

        sns = SNSOperation()
        sns.publish_notification(
            f"Hi! A service request {id} has been deleted.",
            f"Service request deleted")

        return {
            'msg': "Request deleted successfully"
        }
    else:
        return {
            'msg': 'Some error occured',
            'response': response
        }

    
if __name__ == "__main__":
    app.run(debug=True, port=5556)
