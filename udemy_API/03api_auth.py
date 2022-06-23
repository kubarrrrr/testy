import requests

# Authentication
se = requests.session()
se.auth = auth=('kubarrrrr','Haslomaslo2@')

url = "https://api.github.com/users"
github_response = requests.get(url,verify=False,auth=('kubarrrrr', 'Haslomaslo2@'))

print(github_response.status_code)

url2 = "https://api.github.com/users/repos"
response= se.get(url2)
print(response.status_code)