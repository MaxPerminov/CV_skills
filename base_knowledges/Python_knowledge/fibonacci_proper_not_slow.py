#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
n = int(input("> "))
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    first_num, second_num, fib_index = 0, 1, 2
    while True:
        fib_index += 1
        fib_num = first_num + second_num
        if fib_index == n:
            print(fib_num)
            break
        first_num = second_num
        second_num = fib_num
