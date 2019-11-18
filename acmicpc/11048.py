
import sys

N, M = map(int, sys.stdin.readline().split())

l = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    l.append(row)

for i in range(N):
    for j in range(M):

        c = l[i-1][j-1] if 0 < i and 0 < j else 0
        u = l[i-1][j-0] if 0 < i else 0
        a = l[i-0][j-1] if 0 < j else 0

        m = max([c, u, a])
        l[i][j] += m

print(l[N-1][M-1])
    


