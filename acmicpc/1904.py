

import sys

N = int(sys.stdin.readline())

a = 1
b = 2
ret = N

if N == 1:
    print(1%15746)
elif N == 2:
    print(3%15746)
else:
    for i in range(N - 2):
        ret = (a + b) % 15746
        a, b = b, ret
    print(ret%15746)

"""
Cards : 00, 1

N = 1 : 1
N = 2 : 00 11
N = 3 : 100 001 111
N = 4 : 0000 0011 1100 1001 1111
N = 5 : 10000 00100 00001 11001 10011 11100 00111 11111
N = ? : len() = 


1 : 2  : 1
2 : 4  : 2
3 : 8  : 3
4 : 16 : 5
5 : 32 : 8
6 : 64 : 13




"""
