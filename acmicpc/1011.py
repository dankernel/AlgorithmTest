
import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    n = y - x

    temp = math.sqrt(n)
    if math.floor(temp) ** 2 == n:
        print(math.floor(temp * 2)-1)
    else:
        print(math.floor(temp * 2))
