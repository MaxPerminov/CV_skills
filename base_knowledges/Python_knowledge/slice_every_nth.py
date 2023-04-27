def every_nth_1(lst, nth):
    x = slice(nth-1, len(lst)+1, nth)
    return lst[x]


def every_nth2(lst, nth):
    return lst[nth - 1::nth]   # second colon defines step


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(every_nth_1(list_1, 3))
print(every_nth2(list_1, 3))
