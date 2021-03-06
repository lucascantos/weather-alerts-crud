import json
from src.functions.users import UsersHandler
from src.helpers.response import make_response
from src.helpers.validator import validate
from src.schemas import schemas

def fetch_user(event=None, context=None):
    print(event)
    valid_event, v_error = validate(event, schemas.event_schema, remove_requirement=True)
    if v_error:
        return v_error    
    uid = valid_event['pathParameters'].get('uid')
    users_info = UsersHandler()
    if uid:
        user_info = users_info.fetch_user(uid)
        payload = {uid: user_info}
    else:
        payload = {'users': json.dumps(users_info.users)}

    return make_response(payload)

def create_user(event=None, context=None):
    print(event)    
    payload = json.loads(event['body'])
    valid_payload, v_error = validate(payload, schemas.create_schema)
    if v_error:
        return v_error

    users_info = UsersHandler()
    valid_payload = valid_payload['payload']
    if isinstance(valid_payload, list):
        users_info.batch_add_user(valid_payload)
    else:
        users_info.add_user(valid_payload)
    return make_response()


def update_user(event=None, context=None):
    print(event)
    valid_event, v_error = validate(event, schemas.event_schema)
    if v_error:
        return v_error     
    
    payload = json.loads(valid_event['body'])
    valid_payload, v_error = validate(payload, schemas.user_schema,remove_requirement=True)
    if v_error:
        return v_error
    
    uid = valid_event['pathParameters']['uid']
    users_info = UsersHandler()
    users_info.update_user(uid, valid_payload)

    return make_response()

def remove_user(event=None, context=None):
    print(event)
    valid_event, v_error = validate(event, schemas.event_schema)
    if v_error:
        return v_error

    users_info = UsersHandler()
    uid = valid_event['pathParameters'].get('uid')
    users_info.remove_user(uid)
    return make_response({'message': f"User removed: {uid}"})

