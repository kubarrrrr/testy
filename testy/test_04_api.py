import requests
import pytest


def test_reqres():
    r = requests.get('https://reqres.in/api/users?page=2')
    code = r.status_code
    assert code == 200 , 'code doesnt match'
    json_r = r.json()
    print(json_r['total_pages'])
    assert json_r['total_pages'] == 2, 'nie pasuje'
    assert json_r['total'] == 12
    print(json_r['total'])
    print(json_r['data'][0]['email'])
    assert (json_r['data'][0]['email']).endswith('@gmail.com') , 'mail nie pasuje'