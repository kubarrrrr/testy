import pytest
import requests

def test_res():
    response = requests.get('http://google.com')
    assert response.status_code == 200

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"