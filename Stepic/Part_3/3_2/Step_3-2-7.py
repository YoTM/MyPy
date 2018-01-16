def allCount(s, t):
    """
        Ищет вхождение подстроки с ПЕРЕСЕЧЕНИЕМ
    :param s: строка
    :param t: строка
    :return: кол-во вхождений
    """
    s_size = len(s)
    i = 0
    for x in range(s_size):
        if s.startswith(t, x, s_size):
            i += 1
    return i

s = input()
t = input()
print(allCount(s, t))