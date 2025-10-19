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
    alumno_datos = body.get('alumno_datos')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.update_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id},
        UpdateExpression="set alumno_datos=:datos",
        ExpressionAttributeValues={':datos': alumno_datos},
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': 'Alumno actualizado correctamente',
            'resultado': response
        }, default=lambda x: float(x) if isinstance(x, Decimal) else x)
    }