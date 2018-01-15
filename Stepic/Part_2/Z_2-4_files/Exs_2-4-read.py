
f = open("test.txt", "r")
for line in f:
    line = line.rstrip()
    print(repr(line))

x = f.read()
print(repr(x))
f.close()
