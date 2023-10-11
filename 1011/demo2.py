#항목 스캐닝(get)-full scanning

import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table("Movies")
results = table.scan()
# print(type(results)) #dict
# print(type(results.keys()))
# print(results['Count'], results['ScannedCount'])

items = results['Items'] #전체 목록 full scan: items 개수만큼 카운트를 돌면서 i를 찍기 
for i in range(len(items)):
    print(items[i])
    
    