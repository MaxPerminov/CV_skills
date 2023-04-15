try:
    a = int(input("> "))
    if a > 100:
        raise Exception("bigger than 100")
    elif a < 0:
        raise Exception("Not positive")
except Exception as my_error:
    print(my_error)