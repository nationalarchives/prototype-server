from utils import send_query


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
            "Location": 'https://9ofer4y2x6.execute-api.eu-west-2.amazonaws.com/dev/upload?id=%s' % json_response['data']['createCollection']['id'],
        }
    }


