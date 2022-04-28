import requests
import json
# import jsonpath


def test_json_get():
    url = 'https://reqres.in/api/users?page=2'
    res = requests.get(url)
    json_resp = json.loads(res.text)
    pages = res.json()

    # pages = jsonpath.jsonpath(json_resp, 'total_pages')
    # assert pages [0] == 2

    assert pages['total_pages'] == 2