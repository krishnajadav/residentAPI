from urllib import response
from vendors.dynamodb import DynamoDB
from flask import Flask, request, json
from boto3.dynamodb.conditions import Key
import boto3
import uuid

class ServiceRequest:
    def __init__(self):
        self.TABLE_NAME = "t_service_request"
        self.dynamo = DynamoDB()

    def get_all_requests(self):
        return self.dynamo.get_all_records(self.TABLE_NAME)
    
    def insert_service_request(self, data):
        return self.dynamo.insert(self.TABLE_NAME,data)
    
    def delete_service_request(self, id):
        response = self.dynamo.delete(self.TABLE_NAME, id)
    
    def update_service_request(self):
        pass