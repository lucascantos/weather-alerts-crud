import pytest
from handler import create_user
event_list = [
    {'pathParameters': {}},
    {'pathParameters': {'uid': 'test'}},
]
