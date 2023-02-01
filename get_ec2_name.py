import boto3

ec2 = boto3.client('ec2')

def get_instance_name(instance_id):
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]
    tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
    return tags.get('Name', None)

print(get_instance_name("your-instance-id"))
