#항목 스캐닝(get)-index scanning
import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table("Movies")

#1.get_item: key로 스캐닝인덱스 스캐닝 첫번째 방법
result = table.get_item(
    Key = {
    'Code' : '20050112', 'Name' : 'Batman Begins'
    }
)

# print(type(result)) #dict
# print(result.keys())

if __name__ == '__main__':
    print(result['Item'])
