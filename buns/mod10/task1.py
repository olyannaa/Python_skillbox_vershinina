import requests
import json

# Получаем данные о корабле Millennium Falcon
ship_url = 'https://swapi.dev/api/starships/?search=Millennium%20Falcon'
ship_response = requests.get(ship_url)
ship_data = ship_response.json()

# Получаем список пилотов корабля Millennium Falcon
pilots_urls = ship_data['results'][0]['pilots']
pilots_data = []

for pilot_url in pilots_urls:
  pilot_response = requests.get(pilot_url)
  pilot_data = pilot_response.json()

  # Получаем информацию о родной планете пилота
  homeworld_response = requests.get(pilot_data['homeworld'])
  homeworld_data = homeworld_response.json()

  # Добавляем нужную информацию о пилоте в список
  pilot_info = {
  'name': pilot_data['name'],
  'height': pilot_data['height'],
  'weight': pilot_data['mass'],
  'homeworld': pilot_data['homeworld'],
  'homeworld_info': {
  'name': homeworld_data['name'],
  'climate': homeworld_data['climate'],
  'terrain': homeworld_data['terrain']
  }
  }
  pilots_data.append(pilot_info)

# Формируем информацию о корабле и пилотах в виде словаря
ship_info = {
'name': ship_data['results'][0]['name'],
'max_speed': ship_data['results'][0]['max_atmosphering_speed'],
'class': ship_data['results'][0]['starship_class'],
'pilots': pilots_data
}

# Выводим информацию на экран
print(json.dumps(ship_info, indent=4))

# Записываем информацию в JSON-файл
with open('millennium_falcon_info.json', 'w') as json_file:
  json.dump(ship_info, json_file, indent=4)
