
import sys

A = int(sys.stdin.readline())


if 90 <= A and A <= 100:
    print('A')
elif 80 <= A and A <= 89:
    print('B')
elif 70 <= A and A <= 79:
    print('C')
elif 60 <= A and A <= 69:
    print('D')
else:
    print('F')

