from vendors.dynamodb import DynamoDB


class ServiceRequest:
    def __init__(self):
        self.TABLE_NAME = "t_service_request"
        self.dynamo = DynamoDB()

    def get_all_requests(self):
        return self.dynamo.get_all_records(self.TABLE_NAME)