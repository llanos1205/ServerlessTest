import json
import post, get, put


def lambda_handler(event, context):
    method = event['requestContext']['httpMethod']
    if method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": get.get_all(),
                # "location": ip.text.replace("\n", "")
            }),
        }
    elif method == "POST":
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "this is a post",
                # "location": ip.text.replace("\n", "")
            }),
        }
    elif method == "PUT":
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "this is a put",
                # "location": ip.text.replace("\n", "")
            }),
        }
    return {
        "statusCode": 500,
        "body": json.dumps({
            "message": "unmanaged",
            # "location": ip.text.replace("\n", "")
        }),
    }
