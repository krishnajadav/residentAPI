from vendors.dynamodb import DynamoDB

class ServiceRequest:
    def __init__(self):
        self.TABLE_NAME = "t_service_request"

    def get_all_requests(self):
        return DynamoDB.get_all_records(self.TABLE_NAME)