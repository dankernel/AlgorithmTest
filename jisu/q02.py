
import sys

def f(n, k):
    if n == 0 or k == 0 or n < k:
        return 0
    if k == 1:
        return 1
    if k == n:
        return 1

    return f(n-1, k-1) + f(n-k, k)

n = int(sys.stdin.readline())

s = 0
for i in range(1, n + 1):
    
    s += f(n, i)
    print('f(', n, ',', i, ')',f(n, i))

print(s)

