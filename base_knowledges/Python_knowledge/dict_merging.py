x = {'a': 1, 'b': 2}
z = {'c': 3, 'd': 4}
y = {'e': 5, 'f': 6}
result = dict(x, **y, **z)
print(result)
