# modulus division(%) gives a remainder of division without remainder(//):


print(49 % 5)  # = 4

# ----
# explanation:

# 49 // 5 = 9; 9 * 5 = 45; 49 - 45 = 4

# ---
# or
# ---

# 49 // 5 = 9 (9 times to decrease 49 by 5):

# 1)49 - 5 = 44; 2)44 - 5 = 39; 3)39 - 5 = 34; 4)34 - 5 = 29 ...,
# 5)24, 6)19, 7)14, 8)9, 9) = 4

# _____________________________________________________________________________________
print(-49 % 5)  # 1

# ----
# explanation:

# -49 // 5 = -10; -10 * 5 = -50; -49 - (-50) = 1

# ---
# or
# ---
# -49 // 5= -10 (-10 times to decrease(10 times to increase) -49 by 5):
# 1)-49 + 5 = -44; 2)-44 + 5 = -39; 3)-39 + 5 = -34; 4)-34 + 5 = -29 ...,
# 5)-24, 6)-19, 7)-14, 8)-9, 9) -4, 10) = 1


# _____________________________________________________________________________________
print(49 % -5)  # = -1

# ----
# explanation:

# 49//-5=-10; -10 * -5 = 50; 49 - 50 = -1

# ---
# or
# ---
# 49 // -5 = -10 (-10 times to decrease(10 times to increase) 49 by -5):
# 1)49 + (-5) = 44; 2)44 - 5 = 39; 3)39 - 5 = 34; 4)34 - 5 = 29 ...,
# 5)24, 6)19, 7)14, 8)9, 9)4 10)= -1


# _____________________________________________________________________________________
print(-49 % -5)  # = -4

# ----
# explanation:

# -49 // -5 = 9; 9 * -5 = -45; -49 -(-45) = -4

# ---
# or
# ---
# -49 // -5 = 9 (9 times to decrease -49 by -5):
# 1)-49 -(-5) = -44; 2)-44 -(-5) = -39; 3)-39 -(-5) =-34; 4) -34 -(- 5) = -29 ...,
# 5)-24, 6)-19, 7)-14, 8)-9; 9) = -4

# __________
# if positive dividend is lesser than positive divisor or
# negative dividend is greater than negative divisor -

# result equals to dividend:

print(4 % 50000000)  # 4
print(-4 % -50000000)  # -4


# ---
# if dividend is negative and divisor - positive or
# dividend - positive and divisor - negative:

# the result equals to a sum of dividend and divisor:

print(-4 % 50000000)  # 49999996
print(4 % -50000000)  # -49999996

# __________
# if positive dividend is > divisor, and divisor is in (10, 100, 1000...)  -

# the result equals to the last n numbers of the dividend(n equals to quantity of zeroes in divisor):

print(1234567887468489486 % 100000)  # 89486
print(84894 % 10)  # 4
print(848940 % 100)  # 94


# _____________________________________________________________________________________________________
def modulus(a, b):
    return a-a//b*b

# ----


def modulus_decreasing(a, b):
    if b == 0:
        return "ZeroDivisionError: integer modulo by zero"
    if b > 0:
        if a > 0:
            while a > 0:
                a -= b
            if a < 0:
                a += b
        else:
            while a < 0:
                a += b
    elif b < 0:
        if a > 0:
            while a > 0:
                a += b
        else:
            while a < 0:
                a -= b
            if a > 0:
                a += b
    return a


# ____________________________________________________________________________________________________
print(4 % 4)  # 0
print(-4 % 4)  # 0
print(4 % -4)  # 0
print(-4 % -4)  # 0
print(49 % 4)  # 1
print(199 % 198)  # 1
print(12345678 % 16)  # 14
print(24691355 % 12345678)  # 12345677
print(-49 % 4)  # 3
print(-199 % 198)  # 197
print(-12345678 % 16)  # 2
print(-24691355 % 12345678)  # 1
print(49 % -4)  # -3
print(199 % -198)  # -197
print(12345678 % -16)  # -2
print(24691357 % -12345678)  # -12345677
print(-49 % -4)  # -1
print(-199 % -198)  # -1
print(-12345678 % -16)  # -14
print(-24691357 % -12345679)  # -12345678
print(40 % 4)  # 0
print(200 % 10)  # 0
print(12000000 % 60)  # 0
print(12000000 % 3000000)  # 0
print(-40 % 4)  # 0
print(-200 % 10)  # 0
print(-12000000 % 60)  # 0
print(-12000000 % 3000000)  # 0
print(40 % -4)  # 0
print(200 % -10)  # 0
print(12000000 % -60)  # 0
print(12000000 % -3000000)  # 0
print(-40 % -4)  # 0
print(-200 % -10)  # 0
print(-12000000 % -60)  # 0
print(-12000000 % -3000000)  # 0
print(0 % 5)  # 0
print(0 % -5)  # 0
print(4 % 5)  # 4
print(4 % 50000000)  # 4
print(-4 % 5)  # 1
print(-4 % 50000000)  # 49999996
print(4 % -5)  # -1
print(4 % -50000000)  # -49999996
print(-4 % -5)  # -4
print(-4 % -50000000)  # -4
