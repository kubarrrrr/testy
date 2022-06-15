import requests

payload = {'name': 'Kuba', 'job': 'trainee'}

resp = requests.post('https://reqres.in/api/users', data = payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'trainee'