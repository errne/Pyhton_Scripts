import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    tablename = os.environ['TABLE_NAME']
    table = dynamodb.Table(tablename)

    try:
        response = table.delete_item(
        Key={"id": event['id']}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {
        'message': "Delete Item succeeded!"
        }
