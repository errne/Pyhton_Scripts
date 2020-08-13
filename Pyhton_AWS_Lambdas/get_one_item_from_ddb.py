import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
#always start with the lambda_handler
def lambda_handler(event, context):
    # make the connection to dynamodb
    dynamodb = boto3.resource('dynamodb')
    # select the table
    tablename = os.environ['TABLE_NAME']
    table = dynamodb.Table(tablename)
    try:
        response = table.get_item(
        Key={"id": event['id']}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        return {
        'message': "Get Item succeeded!"
        }
