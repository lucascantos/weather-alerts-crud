import pytest
import json
import handler

uid = 'teste01'
payload = {
    'id': uid,
    'latitude': -22,
    'longitude': -44,
    'radius': 30,
    'variable': ['lightning']
}

def test_create():
    create_payload = {'body': json.dumps({'payload': payload})}
    response = handler.create_user(create_payload)
    assert response['statusCode'] == 200

def test_fetch():
    fetch_payload = {'pathParameters': {'uid': uid}}
    response = handler.fetch_user(fetch_payload)
    assert response['statusCode'] == 200

def test_update():
    update_payload = {'pathParameters': {'uid': uid}, 'body': json.dumps({'variables': ['lightning', 'precipitation']})}
    response = handler.update_user(update_payload)
    assert response['statusCode'] == 200

def test_remove():
    remove_payload = {'pathParameters': {'uid': uid}}
    response = handler.remove_user(remove_payload)
    print(response)
    assert response['statusCode'] == 200

def test_fetch_all():
    fetch_payload = {'pathParameters': {'uid': uid}}
    response = handler.fetch_user(fetch_payload)
    assert response['body'] == json.dumps({uid: None})
