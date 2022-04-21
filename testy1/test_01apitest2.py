import requests
import pytest
from requests.auth import HTTPBasicAuth

def test_api():
    r = requests.get('http://httpbin.org/')
    assert (r.status_code) == 200
    

def test_api2():
    r = requests.get('http://httpbin.org/headers')
    assert r.headers["Content-Type"] == "application/json"

def test_location():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body['post code'] == '90210'

# def test_api4():
#     basic = HTTPBasicAuth('user', 'passwd')
#     r = requests.get('https://httpbin.org/basic-auth/', auth=basic)
#     assert r.status_code == 200

