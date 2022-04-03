from flask import current_app

from vendors.helper import Helper


class S3:
    def __init__(self):
        self.bucket_name = current_app.config['BUCKET_NAME']
        self.session = Helper.get_session()
        self.s3 = self.session.client('s3')

    def store_file(self, key, file):
        self.s3.put_object(Body=file, Bucket=self.bucket_name, Key=key)
        url = f"http://{self.bucket_name}.s3.amazonaws.com/{key}"
        return url
