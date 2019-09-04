
import sys

k = int(sys.stdin.readline())

def gcd(a, b):
    while b is not 0:
        r = a % b
        a, b = b, r
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

def d(M, N, x, y):
    l = lcm(M, N)

    if M == x and N == y:
        return l

    for n in range((l//M) + 1):
        temp = M * n + x
        if temp % N == y:
            return temp
        if l < temp:
            return -1

    return -1

for i in range(k):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(d(M, N, x, y))
