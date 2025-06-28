import boto3

ec2 = boto3.client('ec2')

#finding all the snapshots

response = ec2.describe_snapshots(OwnerIds=['self'])

#Finding whether the snapshot is attached to the volume or not
for snapshot in response['Snaphots']:
    snapshot_id = snapshot["SnapshotId"]
    volume_id = snapshot.get('VolumeId')
    if not volume_id:
        print("Deleting snapshot with ID:", snapshot_id)
        ec2.delete_snapshot(snapshot_id)
    else:
        try:
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['Volumes'][0]['Attachments']:
               print("Deleting snapshot with ID:", snapshot_id," as it taken for volume not attached to a running instance.")
               ec2.delete_snapshot(SnapshotId=snapshot_id)
        except ec2.exceptions.ClientError as e:
               if e.response['Error']['Code'] == 'InvalidSnapshot.NotFound':
                  ec2.delete_snapshot(SnapshotId=snapshot_id)
                  print("Snapshot with ID:", snapshot_id, "is deleted as its associated volume not found.")
