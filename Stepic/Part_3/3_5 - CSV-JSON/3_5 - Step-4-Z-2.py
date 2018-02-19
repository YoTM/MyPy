# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов,
#  которые соответствуют классам. У каждого JSON-объекта есть поле name,
#  которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# ﻿Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
# и что никакой класс не наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является
#  и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json

def is_parent(child, parent):
    """
        Рекурсивная ф-я проверки наследования
    :return:
            True - если parent явл-ся прдеком child
            False - если нет
    """
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

# Получаем входные данные в формате JSON
data = json.loads(input())

# Словарь предков
parents = {}

# Словарь результатов вида - класс : кол-во потомков
res_dict = {}

for d in data:
    # Наполняем словарь данными вида класс : предки
    parents[d["name"]] = d["parents"]

for x in parents.keys():
    for y in parents.keys():
        if is_parent(x, y):
            if x in res_dict:
                res_dict[x] += 1
            else:
                res_dict[x] = 1


print(res_dict)