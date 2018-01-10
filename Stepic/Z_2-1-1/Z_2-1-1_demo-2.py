def down(son, son_dict, fix_list):
    """
        Рекурсивная ф-я перебора предков
    """

    if son in son_dict:
        # создаю список предков текущего вызова
        parent_list = son_dict[son]
        #parent_list = reversed(parent_list)
        for p in parent_list:
            #print(parent_list)
            #print('p =', p)
            # если предок уже вызывался
            if p in fix_list:
                # проверка на сам себе предок А:А
                if son in parent_list:
                    if c not in loss_list:
                        loss_list.append(c)
                        print(c)
                        break
                if c not in loss_list:
                    loss_list.append(c)
                    print(c)
                    break
            # если предок не вызывался, то перебираем его предков
            else:
                down(p, son_dict, fix_list)

def check(call_list, son_dict):
    """
        Проверка исключений переданных списком из входных данных
    """

    print('Checking...')
    # Список уже вызванных исключений
    fix_list = []
    # Список отлова лишних исключений
    global loss_list
    loss_list = []

    global c

    for c in call_list:
        # передаю рекурс-ой ф-ии очередной вызов, словарь наследования и список уже вызванных исключений
        down(c, son_dict, fix_list)
        fix_list.append(c)


def prep():
    """
        Обработка входных данных
    """

    # принимаем число классов
    class_count = int(input())

    # Словарь Предков вида - parent: [child-1, child-2, ...]
    parent_dict = {}

    # Список потомков для словаря Предков
    child_dict = {}

    for i in range(class_count):
        # пр-ра заполнения словаря Потомок - Предки
        line = input()
        # если класс унаследован, то заполняем словарь предков
        if ':' in line:
            # список предков
            parent_list = line[line.find(':')+1:].split()

            # Записываем Наследник : список предков в словарь
            child_dict[line[:line.find(':')-1]] = parent_list

    # принимаем кол-во запросов
    q_count = int(input())

    # список исключений
    except_list = []

    # заполнение списка исключений
    for i in range(q_count):
        line = input()
        except_list.append(line)#[:-1])

    # Пр-ра проверки списка исключений на лишние
    # передаю список вызова исключений и словарь наследования
    check(except_list, child_dict)

# НАЧАЛО ПР-МЫ

prep()
