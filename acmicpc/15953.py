
import sys

table_a = [500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
table_b = [512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    a -= 1
    b -= 1

    ret = 0
    if 0 <= a and a < len(table_a):
        ret += table_a[a]
    if 0 <= b and b < len(table_b):
        ret += table_b[b]

    if 0 < ret:
        print('{}{}'.format(ret, '0000'))
    else:
        print(ret)



