import boto3
from flask import Flask, request, json,jsonify
from boto3.dynamodb.conditions import Key
from flask_cors import CORS

client = boto3.client('cognito-idp')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userInfo')

app=Flask(__name__)
CORS(app)
"""if app.config("ENV") == "production":
    app.config.from_object("configs.dev_config.ProductionConfig")
else:
    app.config.from_object("configs.dev_config.DevelopmentConfig")  # add config values in configs folder and
    # retrieve anywhere in the project using app.config("key")"""

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

@app.route("/user/getUserData",methods=['POST','GET'])
def getUserData():
    rows = []
    rows.append({
                'user_id': "1",
                'user_fname': "Krishna",
                'user_lname': "Jadav",
                'user_email': "abc@gmail.com",
                'user_uno': "505",
                'user_pass': "test",
    })

    rows.append({
                'user_id': "2",
                'user_fname': "Vignesh",
                'user_lname': "Nayak",
                'user_email': "test@gmail.com",
                'user_uno': "501",
                'user_pass': "test",
    })

    response = {
        'data': rows,
        'recordsTotal': 5,
        'recordsFiltered': 10,
        'draw': 1,
    }

    return jsonify(response)

@app.route("/user/checkUserData",methods=['POST','GET'])
def checkUserData():
    print(request.form['Id'])
    print(request.form['fname'])
    print(request.form['lname'])
    print(request.form['email'])
    print(request.form['uno'])
    print(request.form['spass'])
    return "1"

@app.route("/user/insertUserData",methods=['POST','GET'])
def insertUserData():
    print(request.form['Id'])
    print(request.form['fname'])
    print(request.form['lname'])
    print(request.form['email'])
    print(request.form['uno'])
    print(request.form['spass'])
    return "1"

@app.route("/user/deleteUserData",methods=['POST','GET'])
def deleteUserData():
    jsonInput = request.get_json()
    ID=jsonInput['ID']
    print(ID)
    return "1"

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

@app.route("/request/getRequestData",methods=['POST','GET'])
def getRequestData():
    
    jsonInput = request.get_json()
    ID=jsonInput['ID']
    print(ID)

    rows = []
    rows.append({
                'request_id': "1",
                'request_category': "Krishna",
                'request_title': "Jadav",
                'request_description': "abc@gmail.com",
                'request_image': "505",
                'request_status': "0",
    })

    rows.append({
                'request_id': "2",
                'request_category': "Vignesh",
                'request_title': "Nayak",
                'request_description': "test@gmail.com",
                'request_image': "501",
                'request_status': "1",
    })

    response = {
        'data': rows,
        'recordsTotal': 5,
        'recordsFiltered': 10,
        'draw': 1,
    }

    return jsonify(response)


@app.route("/request/getAllRequestData",methods=['POST','GET'])
def getAllRequestData():
    
    rows = []
    rows.append({
                'request_id': "1",
                'request_category': "Krishna",
                'request_title': "Jadav",
                'request_description': "abc@gmail.com",
                'request_image': "505",
                'user_uno': "505",
                'user_fname': "Vignesh",
                'request_status': "0",
    })

    rows.append({
                'request_id': "2",
                'request_category': "Vignesh",
                'request_title': "Nayak",
                'request_description': "test@gmail.com",
                'request_image': "501",
                'user_uno': "501",
                'user_fname': "Krishna",
                'request_status': "1",
    })

    response = {
        'data': rows,
        'recordsTotal': 5,
        'recordsFiltered': 10,
        'draw': 1,
    }

    return jsonify(response)

@app.route("/request/insertRequestData",methods=['POST','GET'])
def insertRequestData():
    print(request.form['request_id'])
    print(request.form['request_category'])
    print(request.form['request_title'])
    print(request.form['request_description'])
    print(request.form['user_id'])
    file = request.files['request_image']
    print(file.filename)
    return "1"

@app.route("/request/deleteRequestData",methods=['POST','GET'])
def deleteRequestData():
    jsonInput = request.get_json()
    ID=jsonInput['ID']
    print(ID)
    return "1"

@app.route("/request/changeStatusData",methods=['POST','GET'])
def changeStatusData():
    jsonInput = request.get_json()
    ID=jsonInput['request_id']
    print(ID)
    print(jsonInput['request_status'])
    return "1"

if __name__=="__main__":
    app.run(debug=True)    