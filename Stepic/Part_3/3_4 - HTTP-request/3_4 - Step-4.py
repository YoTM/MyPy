import requests

res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
with open("python-test-image.png", "wb") as f:
    f.write(res.content)
# print(res.text)