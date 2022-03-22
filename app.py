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

@app.route("/user/getUserData",methods=['POST','GET'])
def getUserData():
    class Object:
        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)


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

if __name__=="__main__":
    app.run(debug=True)    