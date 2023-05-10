def decrease_r(array, index=1):
    return array[:-index]


def decrease_l(array, index=1):
    return array[index:]


a = "123456789"

print(decrease_r(a))
print(decrease_r(a, 3))
print(decrease_l(a))
print(decrease_l(a, 3))
