
import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    for j in range(N-i):
        print(' ', end='')
    for k in range(1, i+1):
        print('*', end='')
    print()
