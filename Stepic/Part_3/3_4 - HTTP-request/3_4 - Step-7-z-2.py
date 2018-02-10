import requests
import re

# Получаем ссылку на файл с данными
file_url = "http://pastebin.com/raw/7543p0ns" #input()

# Отправляем get-запрос к странице, выбираем текст из нее
resp = requests.get(file_url).text

# Регулярка для фильра ссылок
link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

links = []

for url in link_pattern.findall(resp):
    # Первым делом — необязательный протокол (http:// или https://),
    # затем последовательность букв, цифр, дефисов, подчёркиваний и точек (домены уровня > 1),
    # потом домен нулевого уровня (от 2 до 6 букв и точек) и В конце домена всегда идет один из знаков / : ' "
    domen = re.search(r'^(https?:\/\/)?([\w+\.-]+\.[a-z\.]{2,6})[/:\'\"]*', url)
    if domen is not None:
        domen = domen.group(2)
        # Проверка на повторы
        if domen not in links:
            links.append(domen)

# Сортируем список результатов
links.sort()
print('\n'.join(links))


# Решение преподавателя:
# import re
# import requests
#
# resp = requests.get(input()).text
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)
#
# for site in sorted(sites):
#     print(site)
