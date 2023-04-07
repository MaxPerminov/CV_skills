import calc_functs
import unittest


class CalcTest(unittest.TestCase):

    """Calc tests"""
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("===========")

    @classmethod
    def tearDownClass(cls):
        """"Tear down Class"""
        print("=============")
        print("tearDownClass")

    def setUp(self) -> None:
        """Set up for test"""
        print("setUp for ["+self.shortDescription()+"]")

    def tearDown(self) -> None:
        """Tear-down test"""
        print("tear down for [" + self.shortDescription() + "]")

    def test_add(self):
        """Add operation test"""
        print("id: "+self.id())
        self.assertEqual(calc_functs.add(1, 2), 3)

    @unittest.skip("Reason")  # to skip test
    def test_sub(self):
        """Sub operation test"""
        print("id: " + self.id())
        self.assertEqual(calc_functs.sub(4, 2), 2)

    def test_mul(self):
        """Mul operation test"""
        print("id: " + self.id())
        self.assertEqual(calc_functs.mul(2, 6), 12)

    def test_div(self):
        """Div operation test"""
        print("id: " + self.id())
        self.assertEqual(calc_functs.div(20, 2), 10)


@unittest.skip("Skip class")  # if you need to skip class
class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc_functs.sqrt(4), 2)

    def test_por(self):
        self.assertEqual(calc_functs.por(4, 2), 16)
