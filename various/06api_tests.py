import requests

payload = {
    "name": "Kuba",
    "job": "Tester"
    }

rp = requests.post('https://reqres.in/api/users', data = payload)
print(rp.json())
assert rp.json() ['job'] == 'Tester'
