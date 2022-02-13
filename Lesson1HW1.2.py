'''2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.'''

import requests
import json

lat = 55.75
lon = 37.61
part = 'hourly,daily'
API_key = '977a5050a49a62ec2adc3c8bf90ff019'
weather_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&units=metric&appid={API_key}'

weather_data = requests.get(weather_url)

with open('weather.json', 'w') as fw:
    json.dump(weather_data.json(), fw)

temp = weather_data.json()['current']['temp']
print(f'{temp} градусов')
