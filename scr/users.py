import json
import boto3
import os

users_table = os.environ["MY_DATABASE"]
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table(users_table)

def getUser(event, context):
    print(json.dumps({"running": True}))
    response=table.get_item(
        Key={
            'pk': 'user',
            'sk': 'age'
        })
    return {
        'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }
    
def putUser(event, context):
    print(json.dumps({"running": True}))
    
    table.put_item(
        Item={
            'pk':'user',
            'sk':'age',
            'name': 'Mikaela',
            'last_name': 'Garcia',
        })
  
    return {
        'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }