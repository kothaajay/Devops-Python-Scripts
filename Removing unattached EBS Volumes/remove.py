import boto3

ec2 = boto3.client('ec2')

#Get all the volumes in AWS account
response = ec2.describe_volumes()

for volumes in response['Volumes']
    volume_id = volumes['VolumeId']
  #check whether volume is attached to ec2 instance
    if not volumes['Attachments']
       print(f"Volume {volume_id} is unattached to ec2 instances and it will be deleted")
       ec2.delete_volumes(volume_id)
    else
       instance_id = volumes['Attachments']['InstanceId']
       print(f"Volume {volume_id} is attached to ec2 instance {instance_id} ")
    

