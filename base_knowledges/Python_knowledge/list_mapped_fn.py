def max_map(lst, fn):
    return max(map(fn, lst))


print(max_map([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']))
