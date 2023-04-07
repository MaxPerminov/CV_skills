# Deque: allows handling different data structures, such as a list, more effectively!


import collections
a = collections.deque()

a.append(1)
a.appendleft("app_left")
print(a)

a.extend(["extend", "end", "delR"])
a.extendleft(["extend2", "left", "delL"])
print(a)

a.pop()
a.popleft()
print(a)

a.rotate(2)  # rotate to the right
print(a)

a.rotate(-1)  # rotate to the left
print(a)
