import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# [] --  можно указать мн-во подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9] -- всё кроме цифр
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]

pattern = r"a.c"
string = "aac"
match_object = re.search(pattern, string)
print(match_object)


string = "abc, a.c, a-c, adc, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
