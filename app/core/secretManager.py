import boto3

class SecretManager:
    def __init__(self, secret):
        self.secret = secret

    def get(self):
        return self.secret