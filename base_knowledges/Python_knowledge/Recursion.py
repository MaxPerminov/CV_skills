# 1)Divide big problem into smaller ones.
# 2)Find base condition
# 3)return base condition to solve all sub-problems


def sums(n):
    if n == 1:
        return 1
    # (n-1) is not an expression, it is a value!!! parameters are not constant, they change during recursion!!!
    return n + sums(n-1)  # 4 + sums(3)  <-3 + sums(2)  <-2 + sums(1) <-1


# print(sums(4))

##########################################################
# Find sum of nums from 1 to 4 with every interim sum
def int_sums(n):
    if n > 0:
        result = n + int_sums(n-1)  # 4 + sums(3)  <-3 + sums(2)  <-2 + sums(1) <-1 + sums(0) <- 0
        print(result)
    else:
        result = 0
    return result


# print(int_sums(4))

##########################################################
# fibonacci nums - list of nums, where every next num is a sum of previous two:
# 0,1,1,2,3,5,8,13

# to make function that counts fibonacci nums: first, index the nums (to understand the function:)
# 0,1,1,2,3,5,8 = 1,2,3,4,5,6,7

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1) + fib(n-2)


# print(fib(6))

# explanation
# fib(6) = fib(5)(l) + fib(4)(r)
# fib(5)(l) = fib(4)(l) + fib(3)(r)
# fib(4)(l) = fib(3)(l) + fib(2)(r)
# fib(3)(l) = fib(2)(l) + fib(1)(r)
# fib(2)(l) = 1
# fib(3)(l) = fib(2)(l)(1) + fib(1)(r)
# fib(1)(r) = 0
# fib(3)(l) = fib(2)(l)(1) + fib(1)(r)(0) = 1
# fib(4)(l) = fib(3)(l)(1) + fib(2)(r)
# fib(2)(r) = 1
# fib(4)(l) = fib(3)(l)(1) + fib(2)(r)(1) = 2
# fib(5)(l) = fib(4)(l)(2) + fib(3)(r)
# fib(3)(r) = fib(2)(l1) + fib(1)(r1)
# fib(2)(l1) = 1
# fib(3)(r) = fib(2)(l1)(1) + fib(1)(r1)
# fib(1)(r1) = 0
# fib(3)(r) = fib(2)(l1)(1) + fib(1)(r1)(0) = 1
# fib(5)(l) = fib(4)(l)(2) + fib(3)(r)(1) = 3
# fib(6) = fib(5)(l)(3) + fib(4)(r)
# fib(4)(r) = fib(3)(l2) + fib(2)(r2)
# fib(3)(l2) = fib(2)(l2) + fib(1)(r2)
# fib(2)(l2) = 1
# fib(3)(l2) = fib(2)(l2)(1) + fib(1)(r2)
# fib(1)(r2) = 0
# fib(3)(l2) = fib(2)(l2)(1) + fib(1)(r2)(0) = 1
# fib(4)(r) = fib(3)(l2)(1) + fib(2)(r2)
# fib(2)(r2) = 1
# fib(4)(r) = fib(3)(l2)(1) + fib(2)(r2)(1) = 2
# fib(6) = fib(5)(l)(3) + fib(4)(r)(2) = 5

##########################################################
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)  # 3 * factorial(3)  <-2 * factorial(1)  <-1


# print(factorial(3))

##########################################################
# the sum of a list of numbers
def sum_list_of_nums(n):
    if len(n) == 1:
        return n[0]
    else:
        # (n[1:]) is not an expression, it is a value!!! It is a list n, that is starting from the second element!!!
        return n[0] + sum_list_of_nums(n[1:])


# print(sum_list_of_nums([3, 15, 8]))

# explanation
# 3 + sum_list_of_nums(n[1:])  <-15 + sum_list_of_nums(n[1:]) <-8

##########################################################
# the sum of a list of numbers (nested)
def list_sum(n):
    total = 0
    for i in n:
        if isinstance(i, list):
            total += list_sum(i)
        else:
            total += i
    return total


# print(list_sum([3, 15, 8, [3, 3, [1]]]))

# explanation
# list_sum([3, 15, 8, [3, 3, [1]]]) = 3 + 15 + 8 + list_sum([3, 3, [1]])
# list_sum([3, 3, [1]]) = 3 + 3 + list_sum([1])
# list_sum([1]) = 1
# (1) + (3 + 3) + (3 + 15 + 8) = 33

##########################################################
# the sum of a non-negative integer

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(int(n / 10))


# print(sum_digits(123))

# explanation
# sum_digits(123) = 3 + sum_digits(12)
# sum_digits(12) = 2 + sum_digits(1)
# sum_digits(1) = 1 + sum_digits(0)
# sum_digits(0) = 0
# (0) + (1) + (2) + (3) = 6

##########################################################
# the sum of the positive integers n+(n-2)+(n-4)... (until n-x =< 0).

def sum_series(n):
    if n < 1:
        return n
    else:
        return n + sum_series(n-2)


# print(sum_series(10))

# explanation
# sum_series(10) = 10 + sum_series(n-2)
# sum_series(8) =  8 + sum_series(n-2)
# sum_series(6) =  6 + sum_series(n-2)
# sum_series(4) =  4 + sum_series(n-2)
# sum_series(2) =  2 + sum_series(n-2)
# sum_series(0) =  0
# (0) + (2) + (4) + (6) + (8) + (10)  = 30

##########################################################
# 'a' to the power 'b'

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


# print(power(3, 4))

# explanation
# power(3, 4) = 3 * power(a, b - 1)
# power(3, 3) = 3 * power(a, b - 1)
# power(3, 2) = 3 * power(a, b - 1)
# power(3, 1) = 3 * power(a, b - 1)
# power(3, 0) = 1
# (1) * (3) * (3) * (3) * (3) = 81

##########################################################
# the greatest common divisor (gcd) of two integers

def gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low, high % low)


print(gcd(12, 16))

# explanation
# gcd(12, 16) = gcd(12, 16 % 12)
# gcd(12, 4) = gcd(4, 12 % 4)
# gcd(4, 0) = 4
