import requests
import re

# Получаем ссылку на файл с данными
file_url = "http://pastebin.com/raw/7543p0ns" #input()

# Отправляем get-запрос к странице, выбираем текст из нее
resp = requests.get(file_url).text

# Регулярка для фильра ссылок
link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
#print(link_pattern.findall(resp))


links = []

for url in link_pattern.findall(resp):
    # links.append(re.search(r'[\w+://][\w+\-*\.][/:\'\"]*', url).group(0))
    links.append(re.search(r'(https?:\/\/)?([\w+\.-]+\.[a-z\.]{2,6})[/:\'\"]*', url).group(2))
    #links.append(re.findall(r'[\w://]?(\w+\.\w+)[/:\'\"]', url))
    # print(links)

links.sort()
print(links)#.sort())
