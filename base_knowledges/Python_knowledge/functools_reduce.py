import functools as f


def to_reduce(x, y):
    return x - y


def reduce_explanation(x, y):
    return x, y


a = [90, 30, 2]
print(f.reduce(to_reduce, a))
b = [90, 30, 2, 1, 0]
print(f.reduce(reduce_explanation, b))
