import boto3
import json
# ec2 = boto3.resource('ec2','us-east-1',aws_access_key_id="AKIAIR6UIQU35YUDU7UQ",
#                       aws_secret_access_key="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")

# client = boto3.client(ec2)
# vpcs = client.describe_regions('us-east-1')
# print(vpcs)
# s3bckts = boto3.resource('s3', aws_access_key_id="AKIAIR6UIQU35YUDU7UQ",
#                        aws_secret_access_key="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")
s3bckts = boto3.resource('s3')
for bucket in s3bckts.buckets.all():
    print(bucket.name)
    
ec2Obj = boto3.resource('ec2')
response = ec2Obj.describe_vpcs().get('vpcs',[])
print (response)