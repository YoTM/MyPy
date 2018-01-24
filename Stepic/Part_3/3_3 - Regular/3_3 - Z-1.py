import sys
import re

pattern = r"(cat.*){2,}"
# pattern = r"(cat).*\1"

for line in sys.stdin:
    line = line.rstrip()
    match = re.search(pattern, line)
    if match:
        print(line)

# Преподаватель:
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)