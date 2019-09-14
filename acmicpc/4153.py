
import sys

while True:

    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break

    l = [a, b, c]
    l.sort()

    if l[0] ** 2 + l[1] ** 2 == l[2]**2:
        print('right')
    else:
        print('wrong')


