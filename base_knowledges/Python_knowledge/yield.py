def f1(x):
    yield x
    yield x ** 3
    yield x ** 4
    

for j in f1(5):
    print(j)

print(*f1(5))
