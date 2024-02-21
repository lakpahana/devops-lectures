#write a lamda function to check the status of the ec2 instance

#create a tag as key : justaname and value : dev
#instance id is i-04553857834cb5248
import json
import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=[
        'i-04553857834cb5248',
    ],
)

print(response)


def lambda_handler(event, context):
    return{
        'statusCode': 200,
    }