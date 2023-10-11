#delete table

import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table("Movies") #테이블 지목

# DeletionProtection 설정 해제
table = table.update(
    DeletionProtectionEnabled=False
)

print(f"Deletion Protection for {table.name} are disabled.")

# 테이블 삭제
table.delete()