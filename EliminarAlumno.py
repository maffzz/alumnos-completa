import boto3
import json

def lambda_handler(event, context):
    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event.get('body', {})

    tenant_id = body.get('tenant_id')
    alumno_id = body.get('alumno_id')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.delete_item(Key={'tenant_id': tenant_id, 'alumno_id': alumno_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Alumno {alumno_id} eliminado correctamente'})
    }