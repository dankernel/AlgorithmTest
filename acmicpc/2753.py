
import sys

Y = int(sys.stdin.readline())


if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
    print(1)
else:
    print(0)
