import re

# pattern = r"Hello (abc|test)"
# string = "Hello abc"
# match = re.match(pattern, string)
# print(match)
# print(match.group())
# print(match.group(0))
# print(match.group(1))

# pattern = r"(\w+)-\1"
# string = "test-test chow-chow"
# duplicates = re.sub(pattern, r"\1",string)
# print(duplicates)

pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)
