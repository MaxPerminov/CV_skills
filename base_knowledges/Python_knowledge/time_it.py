# Time it:

# timeit library is great for timing Python execution times. Just pass a
# function in string format to timeit.timeit() method, and it will carry out
# 1 million executions to report the minimum time the code takes.

# It's very useful to compare small code pieces and different functions
# but can be sluggish with big code.

# Check out the example below demonstrating the execution time difference
# between 2 very similar list comprehension methods in Python and with different number argument:


import timeit
lst1 = "list(range(100))"
lst2 = "[i for i in range(100)]"
a = timeit.timeit(lst1)
b = timeit.timeit(lst2)
c = timeit.timeit(lst2, number=100)  # run it 100 times(default is 1000000)
print(a, b, c, sep="------")
