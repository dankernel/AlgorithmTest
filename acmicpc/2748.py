
import sys

N = int(sys.stdin.readline())

a = 0
b = 1

ret = N
for i in range(N-1):
    ret = a + b
    a, b = b, ret

print(ret)

    

