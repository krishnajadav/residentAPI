from vendors.dynamodb import DynamoDB


class ServiceRequest:
    def __init__(self):
        self.TABLE_NAME = "t_service_request"
        self.dynamo = DynamoDB()

    def get_all_requests(self):
        return self.dynamo.get_all_records(self.TABLE_NAME)
    
    def insert_service_request(self, data):
        return self.dynamo.insert(self.TABLE_NAME,data)
    
    def delete_service_request(self):
        pass
    
    def update_service_request(self):
        pass