import requests
import json


response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rusz Kuba'},)

print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])

response_json = response.json()
print(response_json[0]['isbn'])

print(response.status_code)
assert response.status_code == 200 , 'wrong response'
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

for actualBook in response_json:
    if actualBook['isbn'] == 'ggg1':
        print(actualBook)
        break

expectedBook = {'book_name': 'postman', 'isbn': 'ggg1', 'aisle': '6661'}

assert actualBook == expectedBook ,'different'