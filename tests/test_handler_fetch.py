import pytest
from handler import fetch_user
valid_events = [
    {'pathParameters': {}},
    {'pathParameters': {'uid': 'test'}},
]

@pytest.mark.parametrize("event", valid_events)
def test_valid(event):
    response = fetch_user(event)
    assert response['statusCode'] == 200