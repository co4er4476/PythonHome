#item update

import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table("Movies")
table.update_item(
    
    Key = {
    'Code' : '20050112', 'Name' : 'Batman Begins'
    },
    UpdateExpression='SET Director = :val',
    #  ExpressionAttributeNames={
    #     '': 'string'
    # },
    ExpressionAttributeValues = {
        ':val': 'James Francis Cameron'
        }
)

