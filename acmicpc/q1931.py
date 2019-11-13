
import sys

def s(l):
    return l[2]

N = int(sys.stdin.readline())

l = []
tt = [False] * (2**23)
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    l.append([start, end, end-start])

print(l)
l = sorted(l, key=s)
print(l)

ret = 0
for i in l:
    print(i[0], i[1])
    for j in range(i[0] - 1, i[1] - 1):
        tt[j] = True
    ret += 1

print(ret)

