import os.path

res_list = []
# Рекурсивный обход папок в директории main
for current_dir, dirs, files in os.walk("main"):
    # Дексикографическая сортировка списка директорий
    dirs.sort()
    # Перебираем файлы в списке файлов тек-ей директории
    for file in files:
        # Если файл оканчивается на нужное расширение
        if file.endswith('.py'):
            # Добавляем в список результатов
            res_list.append(current_dir)
            # Выходим из цикла по списку файлов
            break

with open("res-find.txt", "w") as res:
    res.write("\n".join(res_list))
