import boto3
from flask import Flask, request, json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userInfo')

app=Flask(__name__)

@app.route("/user/authentication",methods=['POST','GET'])
def index():
    jsonInput = json.loads(json.dumps(request.json))
    response = table.scan(
        FilterExpression=Key('user_Name').eq(jsonInput['userName']) & Key('user_Password').eq(jsonInput['password'])
    )

    if len(response['Items'])==1:
        return "Authenticate successfully"
    else:
        return "Invalid UserName and Password"

if __name__=="__main__":
    app.run(debug=True)    