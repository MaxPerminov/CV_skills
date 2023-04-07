from collections import Counter

counter = Counter(['Apple', 'Apple', 'Apple', 'Apple', 'Orange', 'Orange', 'Strawberries', 'Strawberries'])
print(counter)

print()
counter2 = Counter(black=1, red=2, blue=3)
print(list(counter2))
print(dict(counter2))
