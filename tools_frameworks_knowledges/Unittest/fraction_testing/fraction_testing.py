import fraction
import unittest


class FracTest(unittest.TestCase):

    def test_FracEq(self):
        self.assertEqual(fraction.Fraction(1, 2),
                         fraction.Fraction(4, 8))

    def test_FracNoEq(self):
        self.assertNotEqual(fraction.Fraction(1, 2),
                            fraction.Fraction(-5, 8))

    def test_FracLes(self):
        self.assertLess(fraction.Fraction(-5, 8),
                        fraction.Fraction(4, 8))

    def test_FracLesEq(self):
        self.assertLessEqual(fraction.Fraction(1, 2),
                             fraction.Fraction(4, 8))

    def test_FracGret(self):
        self.assertGreater(fraction.Fraction(4, 8),
                           fraction.Fraction(-5, 8))

    def test_FracGretEq(self):
        self.assertGreaterEqual(fraction.Fraction(1, 2),
                                fraction.Fraction(-5, 8))

    def test_FracStr(self):
        self.assertEqual(str(fraction.Fraction(1, 2)), "1/2")

    def test_FracStrAbate(self):
        self.assertEqual(str(fraction.Fraction(2, 4)), "1/2")

    def test_FracStrZero(self):
        self.assertEqual(str(fraction.Fraction(0, 2)), "0/1")

    def test_FracStrAbateM(self):
        self.assertEqual(str(fraction.Fraction(-2, 10)), "-1/5")

    def test_add_int(self):
        self.assertEqual(fraction.Fraction(1, 2) +
                         fraction.Fraction(-2, 3), fraction.Fraction(-1, 6))

    def test_add_str(self):
        self.assertEqual(str(fraction.Fraction(1, 2) +
                         fraction.Fraction(-2, 3)), "-1/6")

    def test_sub_int(self):
        self.assertEqual(fraction.Fraction(1, 2) -
                         fraction.Fraction(-2, 3), fraction.Fraction(7, 6))

    def test_sub_str(self):
        self.assertEqual(str(fraction.Fraction(1, 2) -
                         fraction.Fraction(-2, 3)), "7/6")

    def test_mul_int(self):
        self.assertEqual(fraction.Fraction(1, 2) *
                         fraction.Fraction(-2, 3), fraction.Fraction(-1, 3))

    def test_mul_str(self):
        self.assertEqual(str(fraction.Fraction(1, 2) *
                             fraction.Fraction(-2, 3)), "-1/3")

    def test_div_int(self):
        self.assertEqual(fraction.Fraction(1, 2) /
                         fraction.Fraction(-2, 3), fraction.Fraction(-3, 4))

    def test_div_str(self):
        self.assertEqual(str(fraction.Fraction(1, 2) /
                             fraction.Fraction(-2, 3)), "-3/4")
