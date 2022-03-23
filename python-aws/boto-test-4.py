import boto3

resource = boto3.resource('ec2')
client = boto3.client('ec2')

instances = resource.instances.all()

""" for instance in instances:
    resource.create_tags(
        Resources = [
            instance.id
        ],
        Tags = [
            {
                'Key':'test',
                'Value':'this is only a test'
            },
            {
                'Key':'id',
                'Value':instance.id
            },
            {
                'Key':'image',
                'Value':instance.image.name
            }
        ]
    ) """

""" for instance in instances:
    client.delete_tags(
        Resources = [
            instance.id
        ],
        Tags = [
            {
                'Key':'Test',
                'Value':'this is only a test'
            },
            {
                'Key':'Test2',
                'Value':instance.image.name
            }
        ]
    ) """

for instance in instances:
    client.terminate_instances(
        InstanceIds = [
            instance.id
        ],
    )