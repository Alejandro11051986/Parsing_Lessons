'''1. Посмотреть документацию к API GitHub,
разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.'''

import requests
import json

url = 'https://api.github.com'
user = 'Alejandro11051986'
r = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as file_write:
    json.dump(r.json(), file_write)
for i in r.json():
    print(i['name'])
