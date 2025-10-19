import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=Key('tenant_id').eq(tenant_id)
    )
    items = response['Items']
    num_reg = response['Count']
    print(items)

    return {
        'statusCode': 200,
        'tenant_id':tenant_id,
        'num_reg': num_reg,
        'alumnos': items
    }