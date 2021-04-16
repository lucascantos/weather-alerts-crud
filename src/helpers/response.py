import json
def error_message(code, message):
    '''
    Return a response with a code and message
    :params code: int, HTTP error code
    :params message: string, String text of error
    '''
    return make_response(code, {'message': message})

def make_response(body={'message': 'Success!'}, code=200, cors=False):
    '''
    Return a response with a code and message
    :params body: dict, dictionary on JSON format to be sent onwards
    :params code: int, HTTP code of error or success. default = 200, success
    :params cors: bool, True if want to send CORS header in response
    '''
    response = {
        "statusCode": code,
        "body": json.dumps(body)
    }
    if cors:
        response['headers']={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            }
    return response