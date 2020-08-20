import boto3
import os

RunningInstances = []
region = os.environ['EC2_REGION']

def lambda_handler(event, context):

    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        },
        {
            'Name': 'tag:Project',
            'Values': ['Test']
        },
    ]

    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=filters)

    for instance in instances:
        RunningInstances.append(instance.id)

    ec2a = boto3.client('ec2', region_name=region)
    ec2a.stop_instances(InstanceIds=RunningInstances)
