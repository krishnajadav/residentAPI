from urllib import response
import boto3
from flask import current_app

from vendors.helper import Helper


class DynamoDB:

    def __init__(self):
        self.session = Helper.get_session()
        self.resource = self.get_dynamodb_resource()

    def get_dynamodb_resource(self):
        db = current_app.config["DB_NAME"]
        resource = self.session.resource(db, region_name=current_app.config["AWS_REGION"])
        return resource

    def insert(self, table_name, data):
        table_res = self.resource.Table(table_name)
        response = table_res.put_item(
            Item=data
        )
        return response
    
    def delete(self, table_name, id):
        table_res = self.resource.Table(table_name)
        response = table_res.delete_item(
            Key = {
                'request_id': id
            }
        )
        return response

    def get_record(self, table_name, key, value):
        table_res = self.resource.Table(table_name)
        response = table_res.get_item(
            Key={
                key: value
            }
        )
        return response['Items']

    def get_all_records(self, table_name):
        table_res = self.resource.Table(table_name)
        response = table_res.scan()
        return response['Items']
