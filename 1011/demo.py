#sdk로 aws 접속 및 table 생성

import boto3

dynamodb = boto3.resource("dynamodb", region_name='',
                        aws_access_key_id='',
                        aws_secret_access_key='')

client = boto3.client('dynamodb')
list_tables = client.list_tables() #dict
# print(list_tables.keys())
# print(len(list_tables['TableNames']))

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Code',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        }
    ],  
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'Code',
            'KeyType': 'HASH' #파티션키
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE' #정렬키
        }
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Movies'
        }
    ],
    TableClass='STANDARD',
    DeletionProtectionEnabled=True,
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 3
            }
    
    )