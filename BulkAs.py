import requests
from datetime import datetime

town = input('Введите город: ')
# print(result)

key = 'ecc157672d5737c76936a7f7171672de'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': 'town', 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()
print(result['main']['fells_like'])
code = result['cod']

print(f'Температура: {data["temp"]:.1f}\xB0C')
print('Влажность', data['humidity'], '%')
raw_time_sunset = result['sys']['sunset']
print(datetime.utcfromtimestamp(raw_time_sunset).strftime("%H:%M"))
print(f'Координаты:{result["coord"]["lon"]}, {result["coord"]["lat"]}')
print(result['weather'][0]['main'])
if result['weather'][0]['main'] == 'Rain':

 #new

