
import sys

n = int(sys.stdin.readline())

ret = 1
for i in range(1, n + 1):
    ret *= i

print(ret)
