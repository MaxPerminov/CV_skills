# Groups the elements of a list based on the given function and returns the count of elements in each group:

from math import floor


def count(arr, fn=lambda x: x):
    key = {}
    for el in map(fn, arr):
        key[el] = 1 if el not in key else key[el] + 1
    return key


print(count([5.5, 3.2, 5.3], floor))
print(count(['red', 'white', 'orange'], len))


#  count iterable and return dictionary
from collections import Counter

counter = Counter(['Apple', 'Apple', 'Apple', 'Apple', 'Orange', 'Orange', 'Strawberries', 'Strawberries'])
print(counter)

print()
counter2 = Counter(black=1, red=2, blue=3)
print(list(counter2))
print(dict(counter2))
