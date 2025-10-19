import boto3
import json
from decimal import Decimal

def lambda_handler(event, context):
    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event.get('body', {})

    tenant_id = body.get('tenant_id')
    alumno_id = body.get('alumno_id')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(Key={'tenant_id': tenant_id, 'alumno_id': alumno_id})

    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'], default=lambda x: float(x) if isinstance(x, Decimal) else x)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'mensaje': 'Alumno no encontrado'})
        }