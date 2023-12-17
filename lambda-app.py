import json
import boto3
from boto3.dynamodb.conditions import Key
import datetime

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Properties')

def addTime(dic):
  dic["last_updated"] = str(datetime.datetime.now())
  return dic
  
def lambda_handler(event, context):
	

	try:
		if event["action"] == "put":
			data.pop("action")
			data = addTime(event)
			response = table.put_item(Item=data)
			r = table.scan()
		if event["action"] == "update":
			response = table.update_item(
    		Key={'id': event['id'],'county':event['county']},
    		UpdateExpression='SET rent = :new_rent',
    		ExpressionAttributeValues={':new_rent': event["rent"]
    		})
			r = table.scan()
		if event["action"] == "scan":
			r = table.scan()
		if event["action"] == "query":
			response = table.query(
    	KeyConditionExpression=Key('id').eq(event['id']))
			r = response['Items']
		if event["action"] == "delete":
			data = event
			data.pop("action")
			table.delete_item(Key=data)
			#r = data
			r = table.scan()
	except Exception as e:
		r = {"error": str(e)} 

	return {
        'statusCode': 200,
        'body': r
    }
