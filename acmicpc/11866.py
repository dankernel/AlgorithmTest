
import sys

N, K = map(int, sys.stdin.readline().split())

# Init list
l = list(range(1, N + 1))

index = 0
print('<', end='')
while 0 < len(l):

    index += K - 1
    index = index % len(l)

    print(l[index], end='')
    if 1 < len(l):
        print(', ', end='')

    del l[index]

print('>', end='')
