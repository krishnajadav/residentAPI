from flask import current_app
from vendors.helper import Helper


class SNS:

    def __init__(self):
        self.session = Helper.get_session()
        self.resource = self.get_sns_resource()

    def get_sns_resource(self):
        sns = current_app.config["SNS"]
        resource = self.session.resource(sns, region_name=current_app.config["AWS_REGION"])
        return resource

    def publish_notification(self, topic_arn, message, subject):
        topic = self.resource.Topic(topic_arn)
        response = topic.publish(Message=message, Subject=subject)
        return response
