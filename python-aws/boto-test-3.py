import boto3
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
REGION = "us-east-1"
EC2_RESOURCE = boto3.resource(
    'ec2', 
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
    )

instances = EC2_RESOURCE.instances.all()
instance_ids = []

for instance in instances:
    if(instance.state['Code'] == 48):
        """ instance_ids.append(instance.id) """
        print(instance.id)

""" client = boto3.client('ec2')

for instance in instance_ids:
    response = client.terminate_instances(
        InstanceIds = [
            instance
        ],
    ) """