def my_func(x):
    if x >= 3:
        return x


array = {1, 2, 3, 4, 5, False}
print(array)
for i in filter(my_func, array):
    print(i)


##############################
# None as function parameter in filter() removes false from iterable
print(*filter(None, array))
