import requests

# Список чисел для проверки
numbers_lst = []

# Запрашиваем числа для проверки
with open("test2.txt", "r") as file:
    numbers_lst = file.read().splitlines()

params = {
    'json': 'true'
}

for number in numbers_lst:
    # Составляем url для запроса
    api_url = 'http://numbersapi.com/'+number+'/math'
    # Делаем запрос
    res = requests.get(api_url, params=params)
    # Сохраняем словарь данных
    data = res.json()
    with open("result.txt", "a") as file:
        # Есть ли факты о числе?
        flag = data["found"]
        if flag:
            print('Interesting')
            file.write('Interesting'+'\n')
        else:
            print('Boring')
            file.write('Boring' + '\n')
