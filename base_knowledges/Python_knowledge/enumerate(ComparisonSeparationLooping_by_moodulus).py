string1 = ["blue", "red", "pink", "green", "sky"]
for i, j in enumerate(string1, 1):  # i - enumeration, j - iterated list's element, 1 - starting number(0 - default!!!)
    print(i, j)
x = (list(enumerate(string1, 10)))  # returns tuples of pair(enumeration and iterated list's element)
print(x)

#############################################################################
# Pairwise comparison:
x = [10, 20, 30, 40, 10]
for n1, el1 in enumerate(x):
    for n2, el2 in enumerate(x[n1+1:]):
        if el1 == el2:
            print(el1)


# Pairwise comparison of el1 and el2, explanation:
#
# To create enumeration, we also need to specify n1 in outer loop and n2 in inner.
# 1 iteration: n1 = 0; 10 iterates and compares with 20, 30, 40, 10
# 2 iteration: n1 = 1; 20 iterates and compares with 30, 40, 10
# 1 iteration: n1 = 2; 30 iterates and compares with 40, 10
# 1 iteration: n1 = 3; 40 iterates and compares with 10
# 5 iteration: n1 = 4; no output* (x[5] - is not exist)

########################################################################################################
# *while iterating nested for loop, one of iterations is empty - there is no output.

a = [1,2]
b = []

for x in a:
    for y in b:
        print(x)

##############################################################################
# Separating list elements with specified character, using enumerate:

a = [1, 2, 3, 4]

for en, el in enumerate(a):
    if en != 0:
        print(", ", end="")
    print(el, end="")

###########################################################################
# Applying something to all iterations, except for the last:
number = "1243579"
for i, numeral in enumerate(number):
    if i != len(number)-1:
        print(numeral)


# i = (len(number) - 1)  only on last i, so this statement allows
# applying something to all iterations, except for the last.

###########################################################################
# looping iterable's elements using enumerate and modulus division:

x = "abc"
for i in range(8):
    for n, j in enumerate(x):
        print(x[n % len(x)], end=" ")
