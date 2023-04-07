import unittest
import calc_functs_tests


testCases = [calc_functs_tests.CalcTest, calc_functs_tests.CalcExTests]
testLoad = unittest.TestLoader()
suites = []
for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
