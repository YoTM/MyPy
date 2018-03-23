from xml.etree import ElementTree as ET

def get_child(root, scale):
    """
        Ф-я получает "ветку" XML-дерева и вес уровня - перебирает все уровни рекурсивно
    :param root:
    :return:
    """
    # Пока есть подуровни
    for child in root:
        # Увеличиваем ценность уровня
        scale += 1
        # Рекурсивно погружаемся дальше
        get_child(child, scale)
        # Возвращаемся и записываем ценность цвета к общему счету в словаре
        color_scale[child.get('color')] += scale

        # print('check-1')

# tree = ElementTree.parsestring(input())
data = input()
root = ET.fromstring(data)

# Словарь ценности цветов: Красного, Зеленого и Синего
color_scale = {'red': 0,
               'green': 0,
               'blue': 0
               }


start_scale = 1
get_child(root, start_scale)

print(color_scale)


# print(root)
# for child in root:
#     print(child.tag, child.attrib)
