class A:
    def __init__(self):
        self.a = 1

    def two(self):
        self.a = 2


x = A()
print(x.a)
x.two()
print(x.a)
