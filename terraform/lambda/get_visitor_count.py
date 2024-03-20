import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloudresume-test")


def lambda_handler(event, context):
    response = table.update_item(
        Key={ "id":"1"}, 
        UpdateExpression='SET view_counts = view_counts + :incr', 
        ExpressionAttributeValues={':incr': 1} 
        )
    views = table.get_item(Key={"id": "1"})
    # return the updated view count
    return views