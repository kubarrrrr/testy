import requests
import json
import configparser
from utilities.payLoad import *
from utilities.configurations import *
from utilities.resources import *

# delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json= {'ID':'666777898989'},)


url = getConfig()['API']['endpoint'] + ApiResources.addBook
headerss={'Contetn_Type': 'application/json'}
addBook_response = requests.post(url, json=addBookPayload('3563434644'),  headers=headerss, )

print(addBook_response.json())
print('--------------------------\n')
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json["ID"]
print(bookId)

# delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={"ID": bookId})

url2 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headerss={'Contetn_Type': 'application/json'}
delBook_response = requests.post(url2, json={"ID": bookId},  headers=headerss, )


assert delBook_response.status_code == 200
res_json = delBook_response.json()

# print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'
