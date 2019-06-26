from utils import send_query
import json


def handler(event, context):
    query = """
        query GetCollections{
          getCollections{
            collections {
              id,name, legalStatus, closure, copyright
            }
          }
}
    """

    json_response = send_query(event, query)
    return {
        "statusCode": 200,
        "body": json.dumps(json_response['data']['getCollections'])
    }
