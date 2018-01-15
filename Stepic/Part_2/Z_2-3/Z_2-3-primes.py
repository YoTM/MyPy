from math import factorial
import itertools

def primes():
    """
    Ф-я генератор простых чисел (бесконечно)
    :return:
    """
    x = 1
    while True:
        x += 1
        # проверка на "простоту" числа по т. Вильсона
        if (factorial(x-1)+1)%x == 0:
            yield x

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
