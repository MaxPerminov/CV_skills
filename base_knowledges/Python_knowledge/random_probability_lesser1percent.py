import random


a, b, c = 0, 0, 0  # checking probability
for i in (range(100000)):  # to check percents, divide a, b, c by 1000
    if random.random() * 100 <= 0.2:  # probability = 0,2%
        a += 1
    if random.random() <= 0.002:  # probability = 0,2%
        b += 1
    if random.randint(1, 500) == 1:  # probability = 0,2%
        c += 1
print(a)
print(b)
print(c)
