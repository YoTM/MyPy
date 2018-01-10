import os.path
import shutil

# вывод пути текущей папки
print(os.getcwd())
# список содержимого текущей папки
print(os.listdir("tests"))

# Абсолютный путь по относительному
print(os.path.abspath("Exs_2-4-read.py"))

# Рекурсивный обход папок
print("Рекурсивный обход папок")
for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

# Проверка существования файлов и папок
print(os.path.exists("Exs_2-4-read.py"))
print(os.path.exists("Exs_2-4-wat.py"))
print(os.path.exists("tests"))

print(os.path.isfile("Exs_2-4-read.py"))
print(os.path.isfile("tests"))

print(os.path.isdir("Exs_2-4-read.py"))
print(os.path.isdir("tests"))

# Копирование файлов
print("Копирование файлов")
shutil.copy("tests/test1.txt", "tests/test2.txt")
