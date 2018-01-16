
def strReplace(s, a, b):
    i = 0
    if a in b and a in s:
        return 'Impossible'
    else:
        while a in s:
            s = s.replace(a, b)
            i += 1
        return i

s = input()
a = input()
b = input()
print(strReplace(s, a, b))

