dictionary = [
    {1: 200, 2: 300, 3: 0},    # last
    {1: 200, 2: 300, 3: -12},  # third
    {1: 0, 2: 234, 3: -12},  # second
    {1: 0, 2: 2345, 3: -12}  # will be first when sorted
]

# the last sort(1) is the main sort, the first(3) - has the lesser priority
dictionary.sort(key=lambda x: x[3])
dictionary.sort(key=lambda x: x[2], reverse=True)
dictionary.sort(key=lambda x: x[1])

for j in dictionary:
    print(j)

print()

dictionary2 = [
    {1: 100, 2: 10, 3: 100},  # last
    {1: 10, 2: 10, 3: 100},  # third
    {1: 1000, 2: 10, 3: 10},  # second
    {1: 10, 2: 100, 3: 10}  # will be first when sorted
]
# the last sort(x) is the main sort, the first(z) - has the lesser priority
dictionary2_sorted = sorted(sorted(sorted(dictionary2, key=lambda z: z[1]), key=lambda y: y[2],
                            reverse=True), key=lambda x: x[3])

for i in dictionary2_sorted:
    print(i)
