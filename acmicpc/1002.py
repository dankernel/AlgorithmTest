
import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    r = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

    if r == 0:
        if r1 == r2: 
            print(-1)
        else:
            print(0)
    elif r == abs(r1 - r2) or r == abs(r1 + r2):
        print(1)
    elif r < abs(r1 + r2) and abs(r1 - r2) < r:
        print(2)
    else:
        print(0)



