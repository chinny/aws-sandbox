import boto3

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.instances.all()
vms = []
oslist = {"win": 0, "lin": 0}

for instance in instances:
    vms.append(instance.image.name)

for vm in vms:
    if ("windows" in vm) or ("Windows" in vm):
        oslist["win"] += 1
    else:
        oslist["lin"] += 1

print(oslist)