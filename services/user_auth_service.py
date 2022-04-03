from vendors.cognito import Cognito
from vendors.dynamodb import DynamoDB


class UserAuth:

    def __init__(self):
        self.cognito = Cognito()
        self.dynamo = DynamoDB()
        self.table_name = "user"

    def check_if_admin(self, username, password):
        try:
            self.cognito.authorize(username, password)
        except self.cognito.client.exceptions.NotAuthorizedException:
            return None
        except self.cognito.client.exceptions.UserNotConfirmedException:
            return None
        except Exception as e:
            return None
        return "Admin"

    def check_user_in_db(self, username, password):
        filter_dict = {"user_email": username, "user_password": password}
        return self.dynamo.get_record(self.table_name, filter_dict)
