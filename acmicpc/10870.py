
import sys

def f(i):

    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return f(i-1) + f(i-2)

N = int(sys.stdin.readline())
ret = f(N)

print(ret)


