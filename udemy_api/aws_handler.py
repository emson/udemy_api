import boto3
from settings import *

class AwsHandler:
    """Handle the connection to AWS"""

    # def __init__(self):
    #     self.settings = Settings()

    def client(self):
        """Configure boto for AWS"""
        s3_client = boto3.resource('s3')
        return s3_client
