lst = [1, 2, 3, 5, 4, 2, 3, 1, 5, 4, 5]
print(max(set(lst), key=lst.count))
