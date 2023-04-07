dictionary = {"name1": "max", "name2": "anfisa"}
dictionary_switched = {v: k for (k, v) in dictionary.items()}
print(dictionary_switched)

# or using zip

x = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}
y = zip(x.values(), x.keys())
z = dict(y)
print(z)
