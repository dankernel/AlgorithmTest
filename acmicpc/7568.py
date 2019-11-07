
import sys

N = int(sys.stdin.readline())

xl = list()
yl = list()

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    xl.append(x)
    yl.append(y)


print(xl)
print(yl)
