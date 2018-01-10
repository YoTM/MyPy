# -*- coding utf-8 -*-
#!/usr/bin/python3

def check(lst):
    """
        Пр-ра получает на вход список исключений
        Проверяет есть ли у исключения предок и есть ли этот предок в списке вызова исключений
        Проверяет, есть ли у исключения предок среди классов без предков
    :param lst:
    :return:
    """
    count = len(lst)-1
    res = []

    # цикл обработки запросов
    for i in range(count,0):
        for k in range(count, i):
            # если очередное исключение является чьим-то предком из эл-ов ниже по списку,
            # то добавляем его потомка в список лишних

            if find(lst[i], lst[k]) == 'Yes':
                res.append(lst[k])
        print(res)
    # Вывод результата
    for x in lst:
        if x != 0:
            print(x)


def search(parent, child):
    """
        Рекурсивная ф-я поиска в глубину по предкам классов
        Условие выхода - отсутствие очередного класса в словаре или удачный поиск
    """

    global rez

    # класс сам себе предок
    if child == parent:
        # print('класс сам себе предок')
        rez = 'Yes'
        return

    # Получаем список предков по ключу
    parent_list = class_dict.setdefault(child)

    # при достижении корня
    if child == parent_list[0]:
        # print('Корень')
        rez = 'No'
        return

    # Если искомый класс есть в списке предков, то Yes
    if parent in parent_list:
        # print('Нашли!')
        rez = 'Yes'
        return
    else:
        for i in range(len(parent_list)):
            if parent_list[i] in class_dict.keys():
                # если нашли, то выходим из рекурсии
                if rez == 'Yes':
                    return
                # print('Перебор')
                search(parent, parent_list[i])
            else:
                # print('Выход, не нашли')
                rez = 'No'
                return

def find(c1, c2):
    """
        Ф-я выяснения родства классов
    """
    # print(c1,' and ', c2, '?')
    global rez

    # Выставляем отрицательный результат по-умолчанию
    rez = 'No'

    if c1 and c2 in class_dict.keys():
        # если классы есть в словаре
        # вызываем рекурсивную ф-ю
        search(c1, c2)
        # print('Получили ', rez)
        return rez
    else:
        return rez

def start():
    """
        Определяем явл-ся ли класс1 предком классу2

    """
    # принимаем число классов
    class_count = int(input())

    # словарь классов исключений
    global class_dict
    class_dict = {}

    for i in range(class_count):
        # пр-ра заполнения словаря Потомок - Предки
        line = input()
        # если класс унаследован, то забираем список предков
        if ':' in line:
            #line = line.replace(':', '')
            # список предков
            parent_list = line[line.find(':')+1:].split()

            # Записываем Класс - список предков в словарь
            class_dict[line[:line.find(':')-1]] = parent_list

        # иначе - класс сам себе предок)
        else:
            parent_list = [line]
            class_dict[line] = parent_list

    # принимаем кол-во запросов
    q_count = int(input())

    # список исключений
    except_list = []

    # заполнение списка исключений
    for i in range(q_count):
        line = input()
        except_list.append(line)

    # Пр-ра проверки списка исключений на лишние
    check(except_list)


# НАЧАЛО ПРОГ-МЫ
if __name__ == '__main__':
    start()

