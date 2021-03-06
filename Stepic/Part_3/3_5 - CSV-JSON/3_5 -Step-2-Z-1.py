# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv

# Заводим словарь вида: Преступление - кол-во
crimes_dict = {}

# Открываем и читаем файл данных
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    # Перебираем строки
    for row in reader:
        # Выбираем дату
        date = row[2]
        # Выбираем преступление
        crime = row[5]
        # Если в дате есть 2015 год
        if '2015' in date:
            # Если преступления ещё нет в словаре, то добавляем
            if row[5] not in crimes_dict.keys():
                crimes_dict[crime] = 1
            # Иначе суммируем кол-во
            else:
                crimes_dict[crime] += 1

# Находим максимальное среди значений словаря
crime_count = max(crimes_dict.values())
# Перебираем ключ:значение в 2 перем-е
for crime, count in crimes_dict.items():
    # Как только попалась пара с макс-м значением, то выводим соотв. преступ-е
    if count == crime_count:
        print(crime)