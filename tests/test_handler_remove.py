import pytest
from handler import remove_user
event_list = [
    {'pathParameters': {}},
    {'pathParameters': {'uid': 'test'}},
]
