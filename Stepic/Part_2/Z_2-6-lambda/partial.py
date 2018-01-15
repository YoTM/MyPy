import operator as op
from functools import partial

x = int("1101", base=2)
print(x)

int_2 = partial(int, base=2)
x = int_2("1101")
print(x)

x2 = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x2)
sort_by_last(x2)
print(x2)