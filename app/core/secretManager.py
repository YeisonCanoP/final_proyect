import json
import boto3
from botocore.exceptions import ClientError
import sys
sys.path.append('c:/Users/yeiso/OneDrive/Escritorio/Proyecto/final_proyect')
from app.utils.logger import Logger

#Clase para manejar la obtenecion de secretos de AWS Secrets Manager
class SecretManager:

    def __init__(self):
        self.log = Logger("app/logs/SecretManager.log").get_logger()

    def get_secretRDS(self):

        secret_name = "rds!db-01fbdcd9-82e6-4828-b359-052dc8cb396c"
        region_name = "us-east-1"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as ex:
            self.log.warning(f"Error retrieving secret: {ex}")
            raise ex

        secret = get_secret_value_response['SecretString']
        password = json.loads(secret).get('password')
        return password