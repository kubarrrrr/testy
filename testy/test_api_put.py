import requests

import requests

payload = {'name': 'Kuba', 'job': 'trainee'}

resp = requests.post('https://reqres.in/api/users', data = payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'trainee'


payload = {'name': 'Kuba', 'job': 'tester'}

resp = requests.put('https://reqres.in/api/users/2', data = payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'tester'

payload = {'name': 'Kuba'}

resp = requests.patch('https://reqres.in/api/users/2', data = payload)
print(resp)
print(resp.json())
print(resp.headers.get('Content-Type'))
assert resp.json()['name'] == 'Kuba'