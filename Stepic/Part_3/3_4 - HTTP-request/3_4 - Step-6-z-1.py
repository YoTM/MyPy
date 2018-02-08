import requests
import re

# Читаем входные ссылки
link_A = input()
link_B = input()
# Отправляем get-запрос к странице
res = requests.get(link_A)
# Получаем список ссылок со страницы А, декодируем контент из байт-кода в utf-8 (по-умолчанию)
all_link = re.findall(r"<a.*\"(.*)\">",res.content.decode())

flag = "No"

for current_link in all_link:
    res = requests.get(current_link)
    links = re.findall(r"<a.*\"(.*)\">",res.content.decode())
    if link_B in links:
        flag = "Yes"
        break
print(flag)

# Преподаватель:
# import re
# import requests
#
# start_url = input()
# end_url = input()
#
# found = False
#
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
#
# resp = requests.get(start_url).text
# for url in link_pattern.findall(resp):
#     cur_resp = requests.get(url).text
#     if end_url in link_pattern.findall(cur_resp):
#         found = True
#         break
#
# print("Yes" if found else "No")
