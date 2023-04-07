def test(p, q, r):
    print(p, q, r)


test_Dict = {'p': 2, 'q': 4, 'r': 6} 
test_List = [20, 40, 60]

test(*test_Dict)  # p q r
test(**test_Dict)  # 2 4 6
test(*test_List)  # 20 40 60


# You can unpack collections with 1 star notation: *
# You can unpack named collections with 2 star notation: **
# So, if a function takes iterables as argument then you can pass iterables with star notation to such functions.
x = [10, 1, 1, 20, 3, 50, 45, 5, 6]
print(max(*x))
