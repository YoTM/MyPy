import requests
import json
import operator

client_id = '21b6c2ece93d488ce7ce'
client_secret = '43e3ed4d5d82dcfab8529cb485c9e807'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}


# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)

# Словарь для записи ответа сервера
input_dct = {}

# Список идентификаторов для проверки
id_lst = []

# Считываем из файла id для проверки
with open("test3.txt", "r") as file:
    id_lst = file.read().splitlines()

for id in id_lst:
    # Формируем url для запроса
    api_url = 'https://api.artsy.net/api/artists/'+id
    # Инициируем запрос с заголовком
    res = requests.get(api_url, headers=headers)
    # Сохраняем словарь данных
    data = res.json()
    input_dct[data["sortable_name"]] = data["birthday"]

output = sorted(input_dct.items(), key=operator.itemgetter(1, 0))

for i in output:
    print(i[0])