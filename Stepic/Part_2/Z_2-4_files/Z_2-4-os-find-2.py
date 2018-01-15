import os.path

with open("res-find-2.txt", "a") as res:
    # Рекурсивный обход папок в директории main
    for current_dir, dirs, files in os.walk("main"):
        # Дексикографическая сортировка списка директорий
        dirs.sort()
        # Перебираем файлы в списке файлов тек-ей директории
        for file in files:
            # Если файл оканчивается на нужное расширение
            if file.endswith('.py'):
                # Добавляем в список результатов
                res.write(current_dir+"\n")
                # Выходим из цикла по списку файлов
                break
