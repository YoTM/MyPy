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

def get_classes(data_dict):
    """
        Ф-я создаёт набор классов из словаря. Классы не повторяются

    """
    class_set = set()
    for s in data_dict.keys():
        class_set.add(s)
        if data_dict[s] != []:
            for c in data_dict[s]:
                class_set.add(c)
    return class_set


# Получаем входные данные в формате JSON
data = json.loads(input())

# Словарь предков
parents = {}

# Словарь результатов вида - класс : кол-во потомков
res_dict = {}

for d in data:
    # Наполняем словарь данными вида класс : предки
    parents[d["name"]] = d["parents"]

# Создаем мн-во/набор всех классов
all_classes = get_classes(parents)

for current_class in all_classes:
    for c in all_classes:
        if is_parent(c, current_class):
            if current_class in res_dict:
                res_dict[current_class] += 1
            else:
                res_dict[current_class] = 1

for k in sorted(res_dict.keys()):
    print (k, ':', res_dict[k])


# Решение препода:
# import json
#
# data = json.loads(input())
# children = dict()
#
# for cls in data:
#     for par in cls["parents"]:
#         if par not in children:
#             children[par] = []
#         children[par].append(cls["name"])
#
# def dfs(v, used):
#     size = 1
#     used.add(v)
#     if v not in children:
#         return size
#
#     for child in children[v]:
#         if child not in used:
#             size += dfs(child, used)
#
#     return size
#
# ans = []
#
# for cls in data:
#     ans.append((cls["name"], dfs(cls["name"], set())))
#
# for i in sorted(ans):
#     print(i[0], ":", i[1])
