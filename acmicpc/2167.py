
import sys

def printMat(l):
    for i in l:
        print(i)


N, M = map(int, sys.stdin.readline().split())

# input Matrux
l = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    l.append(row)

for j in range(1, M):
    l[0][j] += l[0][j-1]

for i in range(1, N):
    l[i][0] += l[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        l[i][j] += l[i-1][j] + l[i][j-1] - l[i-1][j-1]

# input request
K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())

    x1 = (x-1)
    y1 = (y-1)
    j2 = (j-2)
    i2 = (i-2)

    t = l[x1][y1] if 0 <= x1 and 0 <= y1 else 0
    p = l[i2][j2] if 0 <= i2 and 0 <= j2 else 0
    w = l[x1][j2] if 0 <= x1 and 0 <= j2 else 0
    h = l[i2][y1] if 0 <= i2 and 0 <= y1 else 0
    temp = t - w - h + p
    print(temp)




