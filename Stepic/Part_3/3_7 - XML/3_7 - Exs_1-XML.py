from xml.etree import ElementTree as ET


def get_child(root, scale):
    """
        Ф-я получает "ветку" XML-дерева и вес уровня - перебирает все уровни рекурсивно
    """
    # Увеличиваем ценность уровня
    scale += 1
    color_scale[root.get('color')] += scale

    for child in root:
        # Рекурсивно погружаемся дальше
        get_child(child, scale)

data = input()
root = ET.fromstring(data)

# Словарь ценности цветов: Красного, Зеленого и Синего
color_scale = {'red': 0,
               'green': 0,
               'blue': 0
               }

get_child(root, 0)
print(' '.join(map(str, color_scale.values())))


# Решение преподавателя
# import xml.etree.ElementTree as ET
#
# tree = ET.fromstring(input())
# ans = {"red": 0, "green": 0, "blue": 0}
#
# def dfs(cube, res, depth):
#     res[cube.attrib["color"]] += depth
#     for i in cube.findall("cube"):
#         dfs(i, res, depth + 1)
#
# dfs(tree, ans, 1)
# print(ans["red"], ans["green"], ans["blue"])
