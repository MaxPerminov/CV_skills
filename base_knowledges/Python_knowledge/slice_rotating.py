def slice_rot(array, index):
    return array[index:] + array[:index]


a = "1", "2", "3", "4", "5", "6", "7"
print(slice_rot(a, 2))
