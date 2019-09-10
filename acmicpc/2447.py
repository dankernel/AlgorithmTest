
import sys


def f(index, end, l):
    print('index/end', index, end)
    if index <= end:
        ret = [['*' for i in range(3 ** index)] for j in range(3 ** index)]
        return ret

N = int(sys.stdin.readline())

ret = f(2, N, [['*']])
for i in ret:
    for j in i:
        print(j, end='')
    print()


