# reducing a fraction to the lowest possible form
def abate(n, d, sign):
    x = abs(n)
    y = abs(d)
    while x % y != 0:
        buff_x = x
        buff_y = y
        x = buff_y
        y = buff_x % buff_y
    up_n = abs(n) // y * sign
    up_d = abs(d) // y
    return up_n, up_d


class Fraction:

    # constructing fracture
    def numerator(self):
        return self._numerator

    def denominator(self):
        return self._denominator

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError("The numerator must be an integer")
        if not isinstance(denominator, int):
            raise TypeError("The denominator must be an integer")

        if denominator == 0:
            raise ZeroDivisionError("The denominator can't be zero")

        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if numerator < 0 <= denominator \
                    or numerator >= 0 > denominator:
                sign = -1
            else:
                sign = 1
            (self._numerator, self._denominator) = \
                abate(numerator, denominator, sign)

    def __repr__(self):
        return str(self._numerator) + \
            "/" + str(self._denominator)

    # arithmetic
    def __eq__(self, right):
        left = self
        return left.numerator() == right.numerator() and \
            left.denominator() == right.denominator()

    def __ne__(self, right):
        left = self
        return not left == right

    def __lt__(self, right):
        left = self
        return left.numerator() * right.denominator() < \
            left.denominator() * right.numerator()

    def __le__(self, right):
        left = self
        return not right < left

    def __gt__(self, right):
        left = self
        return right < left

    def __ge__(self, right):
        left = self
        return not right > left

    def __add__(self, right):
        left = self
        a = left.numerator() * right.denominator() + \
            right.numerator() * left.denominator()
        b = left.denominator() * right.denominator()
        return Fraction(a, b)

    def __sub__(self, right):
        left = self
        a = left.numerator() * right.denominator() - \
            right.numerator() * left.denominator()
        b = left.denominator() * right.denominator()
        return Fraction(a, b)

    def __mul__(self, right):
        left = self
        a = left.numerator() * right.numerator()
        b = left.denominator() * right.denominator()
        return Fraction(a, b)

    def __truediv__(self, right):
        left = self
        a = left.numerator() * right.denominator()
        b = left.denominator() * right.numerator()
        return Fraction(a, b)
