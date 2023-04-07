import unittest
import calc_functs_tests


testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(calc_functs_tests)
runner = unittest.TextTestRunner(verbosity=2)  # 1 or 2: 2 gives more info than 1
testStat = runner.run(suites)
print("errors")
print(len(testStat.errors))
print("failures")
print(len(testStat.failures))
print("skipped")
print(len(testStat.skipped))
print("testRun")
print(testStat.testsRun)
