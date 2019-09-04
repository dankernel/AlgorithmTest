
import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())


    F = N % H
    Ho = (N // H) + 1
    if F == 0:
        F = H
        Ho -= 1

    print('%d%02d'%(F, Ho))
