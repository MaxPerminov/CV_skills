class Test:

    @staticmethod
    def a():
        return 1

    @staticmethod
    def b():
        return 2


# different quantity of method parameters
class Test2:

    @staticmethod
    def fn_a(x, y):
        print(x, y)

    @staticmethod
    def fn_b(x, y, z):
        print(x, y, z)
