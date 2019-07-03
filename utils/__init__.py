from botocore.vendored import requests


def get_token(event):
    if 'authorizationToken' in event:
        auth_header = event['authorizationToken']
    elif 'cookie' in event['headers']:
        auth_header = event['headers']['cookie']
    else:
        auth_header = event['headers']['Cookie']
    return auth_header.split("=")[1]


def send_query(event, query):
    print(event)
    token = get_token(event)
    headers = {'Authorization': token}
    url = "https://qad2wpgi3befniyihgl42yvfea.appsync-api.eu-west-2.amazonaws.com/graphql"
    response = requests.post(url, json={"query": query}, headers=headers)
    print(response.status_code)
    json_response = response.json()
    return json_response
