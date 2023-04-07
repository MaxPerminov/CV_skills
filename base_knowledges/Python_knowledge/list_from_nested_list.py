# several 1 level nested lists
a = [[1, 2, 3], [78, 456, 4, 5, 6]]

print("Original List:", a)

result = []
for sublist in a:
    for item in sublist:
        result.append(item)

print("like this", result)

# or

result = (sum(a, []))
print("the same", result)

# or


def flatten(lst):
    return [x for y in lst for x in y]


print("same again", flatten(a))


# nested_nested:


from collections.abc import Iterable


def deep_flatten(lst):
    return [x for i in lst for x in deep_flatten(i)] if isinstance(lst, Iterable) else [lst]


b = [1, [2], [[3], 4], 5]
print(f"\nOriginal nested List: {b}\nresult: {deep_flatten(b)}")
