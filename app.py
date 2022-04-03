import uuid
from crypt import methods
import boto3
from flask import Flask, request, json, jsonify
from boto3.dynamodb.conditions import Key
from entities.service_request import ServiceRequest
from entities.sns_operation import SNSOperation
from flask_cors import CORS

import logging

app = Flask(__name__)
CORS(app)

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
        requests = service_request.get_all_requests()
        response = {
            'data': requests,
        }
        # sns = SNSOperation()
        # sns.publish_notification("GET Requested", "By Admin")

        return jsonify(response)
    except Exception as e:
        logging.log(e.args)
        return "Exception occurred", 500


@app.route("/upsert-service-request", methods=['POST'])
def store_service_request():
    json_data = request.form
    request_id = json_data["request_id"]    # if 0 insert, else update
    request_category = json_data["request_category"]
    request_title = json_data["request_title"]
    request_description = json_data["request_description"]
    user_id = json_data["user_id"]
    request_image = request.files["request_image"]
    request_image = request_image.name
    print(request_image)

    try:
        service_request = ServiceRequest()
        data = {
            "user_id": user_id,
            "request_category": request_category,
            "request_title": request_title,
            "request_description": request_description,
            "request_image": request_image
        }

        if request_id == '0':
            data["request_id"] = str(uuid.uuid4())
            print(f"inside insert \n data== {data}")
            service_request.insert_service_request(data)
        else:
            print(f"inside update \n data== {data}\n request_id= {request_id}")
            service_request.update_service_request(request_id, data)

        # sns = SNSOperation()
        # sns.publish_notification(
        #     f"Hi! You have a new service request: \n Request ID: {request_id} \n Request Title: {request_title}",
        #     f"New Service Request from {user_id}")

        return str(1), 200

    except Exception as e:
        logging.log(e.args)
        return "Exception occured", 500


@app.route("/delete-request", methods=['DELETE'])
def delete_request():
    try:
        json_input = request.get_json()
        request_id = json_input['ID']
        service_request = ServiceRequest()
        service_request.delete_service_request(request_id)
        # sns = SNSOperation()
        # sns.publish_notification(
        #     f"Hi! A service request {id} has been deleted.",
        #     f"Service request deleted")
        return "1", 200
    except Exception as e:
        return {
            'msg': 'Some error occured',
            'trace': e.with_traceback()
        }


if __name__ == "__main__":
    app.run(debug=True, port=5556)
