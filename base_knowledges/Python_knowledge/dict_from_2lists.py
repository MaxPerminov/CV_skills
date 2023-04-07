list_a = ["1", "2", "3"]
list_b = ["a", "b", "c"]

dict_a_b = {}
for i in range(len(list_a)):
    key = list_a[i]
    dict_a_b[key] = list_b[i]
print(dict_a_b)  # {'1': 'a', '2': 'b', '3': 'c'}

# or

dict_a_b_compr = {list_a[i]: list_b[i] for i in range(len(list_a))}
print(dict_a_b_compr)  # {'1': 'a', '2': 'b', '3': 'c'}
