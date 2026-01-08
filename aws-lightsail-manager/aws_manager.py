import boto3

def get_lightsail(region):
    return boto3.client("lightsail", region_name=region)

def start_instance(instance_name, region):
    client = get_lightsail(region)
    client.start_instance(instanceName=instance_name)

def stop_instance(instance_name, region):
    client = get_lightsail(region)
    client.stop_instance(instanceName=instance_name)

def get_status(instance_name, region):
    client = get_lightsail(region)
    response = client.get_instance(instanceName=instance_name)
    return response["instance"]["state"]["name"]
