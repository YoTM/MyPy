import requests

res = requests.get("https://yandex.ru/search/",
                   params={
                       "text": "Stepic",
                   })
print(res.status_code)
print(res.headers['Content-Type'])

print(res.url)
print(res)
#print(res.text)