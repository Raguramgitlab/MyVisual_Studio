import boto3
x = boto3.resource('ec2')
x.create_instances(ImageId='ami-0c802847a7dd848c0',InstanceType='t2.micro',KeyName='AWSkey',MinCount=1,MaxCount=1)
client = boto3.client('ec2')
client.terminate_instances(
    InstanceIds=['i-077eedcdaa8e433fd'])