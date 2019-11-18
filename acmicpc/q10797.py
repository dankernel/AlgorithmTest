
import sys

N = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

ret = 0
for i in l:
    if N == i:
        ret += 1
print(ret)
