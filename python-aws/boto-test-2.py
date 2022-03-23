import boto3
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
REGION = "us-east-1"
client = boto3.client(
    'ec2', 
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
)

response = client.describe_instances()

for r in response['Reservations']:
    print(r['Instances'][0]['InstanceId'])
    print(r['Instances'][0]['ImageName'])