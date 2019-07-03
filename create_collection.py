from utils import send_query
import os


def handler(event, context):
    
    query = """
        mutation {
           createCollection(name: "test", copyright: "copyright", closure: "closure", legalStatus: "legalStatus") {
              id
           }
    }
    """
    json_response = send_query(event, query)

    return {
        "statusCode": 301,
        "headers": {
            "Location": '%s/upload?id=%s' % (os.environ['REDIRECT_URL'], json_response['data']['createCollection']['id'],)
        }
    }


