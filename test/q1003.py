
import sys

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        print('1 0')
    elif num == 1:
        print('0 1')
    elif num == 2:
        print('1 1')
    else:
        a = 0
        b = 1
        ret = 0
        for j in range(num - 1):
            ret = a + b
            a, b = b, ret

        print(a, b)


