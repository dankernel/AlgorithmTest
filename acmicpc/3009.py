
import sys

xl = []
yl = []

for i in range(3):
    x, y = list(map(int, sys.stdin.readline().split()))

    if x in xl:
        del xl[xl.index(x)]
    else:
        xl.append(x)

    if y in yl:
        del yl[yl.index(y)]
    else:
        yl.append(y)
        
print(xl[0], yl[0])

