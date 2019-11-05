
import sys

N = int(sys.stdin.readline())

expMap = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6, 4, 6],
        [5, 5, 5, 5],
        [6, 6, 6, 6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1, 9, 1]]

for i in range(N):
    a, b = (list(map(int, sys.stdin.readline().split())))

    ret = expMap[a % 10][(b % 4) - 1]
    if ret == 0:
        ret = 10
    print(ret)

