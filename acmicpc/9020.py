
import sys
import math

T = int(sys.stdin.readline())

def f(n):

    tb = [True] * (n + 1)
    tb[0] = False
    tb[1] = False

    for i in range(2, n+1):
        if tb[i] == True:
            for j in range(2, (n//i) + 1):
                tb[i * j] = False

    return tb

for i in range(T):
    n = int(sys.stdin.readline())

    ret = []
    tb = f(n)
    for i in range(int(len(tb)/2) + 1):
        if tb[i] == True:
            if tb[n-i] == True:
                ret.append([i, n-i])
    
    print(ret[-1][0], ret[-1][1])

