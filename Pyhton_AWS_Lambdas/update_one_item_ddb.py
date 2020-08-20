import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    id = event['id']

    response = table.update_item(
        Key={
            "id": id
        },
        UpdateExpression="set forename = :f, surname = :s, title = :t, dob = :d, gp = :g, phone = :p, email = :e",
        ExpressionAttributeValues={
            ":f": event['forename'],
            ":s": event['surname'],
            ":t": event['title'],
            ":d": event['dob'],
            ":g": event['gp'],
            ":p": event['phone'],
            ":e": event['email']
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
