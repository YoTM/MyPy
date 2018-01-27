import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'.*z\w{3,3}z.*', line):
        print(line)