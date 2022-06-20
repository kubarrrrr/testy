import requests
import json

# delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={'ID':'777423234'},)

addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json={

"name":"Learn Appium Automation with Java",
"isbn":"7774",
"aisle":"23234",
"author":"John foe"
}, headers = {'Contetn_Type' : 'application/json'},)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
# print(bookId)

delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={'ID':'777423234'},)

assert delBook_response.status_code == 200
res_json = delBook_response.json()

print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'