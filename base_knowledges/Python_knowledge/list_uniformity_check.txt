# Checks if all elements in a list are equal:
def uniformity(lst):
    return lst[1:] == lst[:-1]


print(uniformity([1, 2, 4, 6, 8, 10])) 
print(uniformity([2, 2, 2, 2]))
