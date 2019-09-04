
import sys

def f(n, i):

    if n - i <= 0:
        return 0
    print(n)
    return f(f(n, n-1), f(i, n-i))

N = int(sys.stdin.readline())

f(N, 0)

