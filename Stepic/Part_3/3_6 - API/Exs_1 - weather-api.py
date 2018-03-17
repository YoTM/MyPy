import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

# Запрашиваем город у пользователя
city = input("City? ")

params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# # Получаем статус-код ответа на запрос
# print(res.status_code)
# # Получаем тип содержимое ответа
# print(res.headers["Content-Type"])
# # Получаем содержимое ответа
# print(res.json()) # returns json.loads(res.text)

# Сохраняем словарь данных
data = res.json()
template = 'Current temperature in {} is {}'
# Выводим значения ключей
print(template.format(city, data["main"]["temp"]))