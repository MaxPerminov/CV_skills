# Simple function:
def fn(a):
    print("basis fn: ", a)
    return a + 1


print("name: ", fn.__name__)
print("doc: ", fn.__doc__)
b = fn(1)


# to check the callability of an object:
print(callable(fn))

########################################################################################
# Decorators take the function and add new instructions to it. It consists of:
# 1)decorator-function - takes as an argument function, that will be decorated

# 2)wrapper-function - decorates function, that was taken as an argument by
# decorator-function. It can access the outer local functions!!!

# 3)decorated-function - goes as argument to decorator-function.


def decor(fn):
    def wrapper():
        return fn()+1
    return wrapper


def basic():
    return 1


wrapped = decor(basic)


# or :

def decor(fn):
    def wrapper():
        return fn()+1
    return wrapper


@decor
def basic():
    return 1


print(basic())
##########################################################################


def decor(fn):
    def act(x, y):                  ###wrapper function takes the same number of parameters
                                    # as decorated-function// or can take * and ** parameters!!!
        return fn(x*10, y*10)
    return act


@decor
def a(b, c):
    return b + c


print(a(1, 2))

#################################################################
# Chaining decorators


def d1(fn):
    def inner():

        return fn() + 1
    return inner


def d2(fn):
    def inner():

        return fn() / 2
    return inner

@d2
@d1
def funct():
    return 1


a = funct()
print(a)

###########################################################
# Decorator with parameters


def d1(x):

    def inner(fn):
        def inner1():
            return fn() + 1 + x
        return inner1
    return inner


@d1(1)
def funct():
    return 1


a = funct()
print(a)
