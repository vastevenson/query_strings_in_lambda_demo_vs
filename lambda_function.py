import json

def lambda_handler(event, context):
	print({"event": event, "context": context})
	if event['queryStringParameters']['x']:
    	x = event['queryStringParameters']['x']
	if event['queryStringParameters']['y']:
    	y = event['queryStringParameters']['y']
    
	content = f"<p>The sum of {x} and {y} is {adder(x,y)}</p>"
    
	response = {
    	"statusCode": 200,
    	"statusDescription": "200 OK",
    	"isBase64Encoded": False,
    	"headers": {
        	'Content-Type': 'text/html',
    	},
    	"body": content
	}
	return response

def adder(x,y):
	x = int(x)
	y = int(y)
	return x+y

