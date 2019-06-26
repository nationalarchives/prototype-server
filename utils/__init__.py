from botocore.vendored import requests


def send_query(event, query):
    print(event)
    token = event['headers']['Cookie'].split("=")[1]
    headers = {'Authorization': token}
    url = "https://qad2wpgi3befniyihgl42yvfea.appsync-api.eu-west-2.amazonaws.com/graphql"
    response = requests.post(url, json={"query": query}, headers=headers)
    print(response.status_code)
    json_response = response.json()
    return json_response
