
import sys

N, K = map(int, sys.stdin.readline().split())


l = list(range(1, N + 1))

print(l)

i = 0
j = 0
while 0 < len(l):

    i += 3 - j

    if len(l) < i:
        i = i % len(i)

    print(l[i - 1])
    j += 1

