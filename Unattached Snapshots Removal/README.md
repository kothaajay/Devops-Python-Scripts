In this python script we will find unattached snapshots to ec2 instances, volumes and remove them.

First we need to fetch all the instance ids, then we need to filter out snapshots and volume ids of instances.

Then we need to remove the snapshots which are unattached.
