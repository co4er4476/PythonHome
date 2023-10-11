import boto3

resource = boto3.resource("dynamodb", region_name='',
               aws_access_key_id='',
               aws_secret_access_key='') #사전 로그인 안했다면 이 정보로 로그인진행

# print(resource)
# client = boto3.client('dynamodb')
# print(client.list_tables())

# table = client.describe_table(
#     TableName = 'lab-movie'
# )
# print(table)

table = resource.Table('lab-movie')

item = {
  'Code': '19780080',
  'Name': 'test movie',
  'Genre': 'Romance',
  'Date': '1978-04-12',
  'Director': 'AA',
  'Actor': '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
  }
table.put_item(Item=item)