
import sys

def shiftR(l):
    temp = l[-1]
    del l[-1]
    l.insert(0, temp)
    return l

def shiftL(l):
    temp = l[0]
    del l[0]
    l.append(temp)
    return l

def pic(l):
    del l[0]

N, M = map(int, sys.stdin.readline().split())
select = list(map(int, sys.stdin.readline().split()))

l = list(range(1, N + 1))
ret = 0

for i in select:
    index = l.index(i)

    d = 0
    if index < len(l)/2:
        d = index
    else:
        d = index - len(l)

    if 0 < d:
        for j in range(d):
            shiftL(l)
            ret += 1
    else:
        for j in range(-d):
            shiftR(l)
            ret += 1

    pic(l)


print(ret)
