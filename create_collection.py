from utils import send_query
import os



def handler(event, context):
    collectionName = event['body'].split("=",1)[1]
    query = """
        mutation {
           createCollection(name: "%s", copyright: "copyright", closure: "closure", legalStatus: "legalStatus") {
              id
           }
    }
    """ %(collectionName)

    json_response = send_query(event, query)

    return {
        "statusCode": 301,
        "headers": {
            "Location": '%s/upload?id=%s' % (os.environ['REDIRECT_URL'], json_response['data']['createCollection']['id'],)
        }
    }


