import boto3

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.instances.all()
instance_ids = []

for instance in instances:
    instance_ids.append(instance.id)

tag_creation = EC2_RESOURCE.create_tags(
    Resources =
        instance_ids,
    Tags = [
        {
            'Key':'Test',
            'Value':'this is only a test'
        },
        {
            'Key':'Test2',
            'Value':'this is another test'
        },
    ]
)