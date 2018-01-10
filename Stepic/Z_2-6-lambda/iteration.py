x = input().split()
print(x)
map_obj = map(int, x) # f [a, b, c, ...] -> f(a0, f(b), f(c) ...
print(map_obj)
n = next(map_obj)
k = next(map_obj)
print(n+k)