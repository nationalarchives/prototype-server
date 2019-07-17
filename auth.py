from jwt import (
    JWT, jwk_from_dict
)
import requests
from http import cookies


def create_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource
                }
            ]
        }
    }


def get_token(event):
    if 'authorizationToken' in event:
        auth_header = event['authorizationToken']
    elif 'cookie' in event['headers']:
        auth_header = event['headers']['cookie']
    else:
        auth_header = event['headers']['Cookie']
    token = cookies.SimpleCookie(auth_header)['token'].value
    return token


def handler(event, context):
    print(event)
    token = get_token(event)
    decoded = verify_token(token)
    print(decoded)
    if decoded is not None:
        return create_policy(decoded['email'], "Allow", event["methodArn"])
    else:
        return create_policy("unauthorised", "Deny", event["methodArn"])


def verify_token(token):
    region = 'eu-west-2'
    userpool_id = 'eu-west-2_6Mn0M2i9C'
    keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(
        region, userpool_id)
    response = requests.get(keys_url).json()
    try:
        for key in response["keys"]:
            verifying_key = jwk_from_dict(key)
            jwt = JWT()
            return jwt.decode(token, verifying_key)
    except Exception as e:
        print(e)
        return None
