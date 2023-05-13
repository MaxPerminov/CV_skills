def recursion(arr, index):
    arr[index] = "q"
    if index in range(len(arr) - 1):
        recursion(arr, index + 1)


a = [1, 2, 3, 4, 5, 6, 7]
recursion(a, 1)
print(a)
