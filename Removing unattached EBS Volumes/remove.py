import boto3

ec2 = boto3.client('ec2')

#Get all the volumes in AWS account
response = ec2.describe_volumes(OwnerIds=['self'])

for volumes in response

