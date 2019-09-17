
import sys

N = int(sys.stdin.readline()) + 1

l = []
l.append(0)
l.append(0)
l.append(1)
l.append(1)

if N == 2:
    print(0)
    exit()
for i in range(4, N):

    temp = []
    if i % 2 == 0:
        temp.append(l[int(i/2)])
    if i % 3 == 0:
        temp.append(l[int(i/3)])
    temp.append(l[i-1])

    m = min(temp)
    l.append(m+1)

print(l[-1])

