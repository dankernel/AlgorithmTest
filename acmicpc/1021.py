
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

l = list(range(1, N + 1))
pic(l)
print(l)

