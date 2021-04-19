import pytest
from handler import fetch_user
event_list = [
    {'pathParameters': {}},
    {'pathParameters': {'uid': 'test'}},
]
