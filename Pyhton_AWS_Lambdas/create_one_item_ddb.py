import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)

    client = event
    id = str(uuid.uuid1())
    client["id"] = id

    response = table.put_item(
       Item = client
    )
    return response
