import json
from botocore.vendored import requests

def lambda_handler(event, context):
    
    query = """
        mutation {
           createCollection(collection: {name: "test", copyright: "copyright", closure: "closure", legalStatus: ""}) {
              id
           }
    }
    """
    token = event['headers']['Cookie'].split("=")[1]
    headers = {'Authorization': 'Bearer %s' % token}
    print(json.dumps(headers))
    print(json.dumps({"query": query}))
    url = "https://m6t2cgd8uc.execute-api.eu-west-2.amazonaws.com/dev/graphql"
    response = requests.post(url, json={"query": query}, headers=headers)
    print(response.status_code)
    json_response = response.json()
    id = json_response['data']['createCollection']['id']
    return {
        "statusCode": 301,
        "headers": {
            "Location": 'https://9ofer4y2x6.execute-api.eu-west-2.amazonaws.com/dev/upload?id=%s' % id,
        }
        
    };
    
