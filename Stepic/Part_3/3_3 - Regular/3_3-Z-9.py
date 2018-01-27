# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
#
# Sample Input:
#
# attraction
# buzzzz
#
# Sample Output:
#
# atraction
# buz

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'((\w)\2+)', r'\2', line))

# Преподаватель
# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     line = re.sub(r"(\w)\1+", r"\1", line)
#     print(line)