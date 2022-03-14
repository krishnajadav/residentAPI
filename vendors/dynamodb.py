import boto3
from flask import current_app


class DynamoDB:

    def __init__(self):
        self.resource = self.get_dynamodb_resource()

    @staticmethod
    def get_dynamodb_resource():
        db = current_app.config("DB_NAME")
        access_key = current_app.config("AWS_ACCESS_KEY_ID")
        secret_key = current_app.config("AWS_SECRET_ACCESS_KEY")
        region = current_app.config("AWS_REGION")
        resource = boto3.resource(
            db,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        return resource

    def insert(self, table_name, data):
        table_res = self.resource.Table(table_name)
        response = table_res.put_item(
            Item=data
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
