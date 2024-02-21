#write a lamda function to check the status of the ec2 instance
import json
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }