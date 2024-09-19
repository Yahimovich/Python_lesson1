import pytest
import requests
from requests import request
from 08_lesson.constanse import URL  

@pytest.fixture()
def get_token(username='flora', password='nature-fairy'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(URL + '/auth/login', json=log_pass)
    token = resp_token.json()[userToken] 
    return token

