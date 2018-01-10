x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0

evens = list(filter(even, xs))
print(evens)

