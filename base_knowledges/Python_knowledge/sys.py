# sys.exit("some error message") is a quick way to exit a program.

import sys


a = int(input())
if a == 0:
    sys.exit()
print(1 / a)
