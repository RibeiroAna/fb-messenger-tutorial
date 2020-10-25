import json
import urllib3
import boto3
import os


MIN_CONFIDENCE = 0.6
ENTITIES = "Entities"
INTENT = "Intent"
REGION = "us-east-1"
TABLE = "IntentTable"
ERROR_ANSWER = "Sorry, I didn't Understand!"
OTHER = "Other"


def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = decide_answer(body)
    send_response(message, body)


def decide_answer(body):
    nlp_entities = body['entry'][0]['messaging'][0]['message']['nlp']['entities']
    
    if ('intent' in nlp_entities) and (nlp_entities['intent'][0]['confidence'] > MIN_CONFIDENCE):
        dynamodb = boto3.resource('dynamodb', region_name = REGION)
        table = dynamodb.Table(TABLE)
        try:
            # Querying the database
            table_item = table.get_item(Key={'Intent': nlp_entities['intent'][0]['value']})['Item']

            # Looking for a direct answer
            if('answer' in table_item):
                return table_item['answer']
            else:
                # Checking if the message has a valid entity
                entity = list(table_item.keys() & nlp_entities.keys())
                if len(entity) == 1:
                    entity_value = nlp_entities[entity[0]][0]['value']
                    if(entity_value in table_item[entity[0]]) and (nlp_entities[entity[0]][0]['confidence'] > MIN_CONFIDENCE):
                        return table_item[entity[0]][entity_value]
                    else:
                        return table_item[entity[0]][OTHER]
        except:
            return ERROR_ANSWER
           
    return ERROR_ANSWER


def send_response(message, body):
    token = os.environ['FB_TOKEN']
    url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + token
    payload = {
        'recipient': body['entry'][0]['messaging'][0]['sender'],
        'message': {
            "text": message
        }
    }
    requests = urllib3.PoolManager()
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request(
        'POST',
        url,
        body=json.dumps(payload),
        headers=headers
    )