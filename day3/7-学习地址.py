
a = [1, 2, 3]
b = a.copy()
print(id(a))
print(id(b))
a[0] = 10
print(b)
