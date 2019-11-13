
import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()

ll = [l[0]]
for i in range(1, len(l)):
    ll.append(l[i]+ ll[i-1])

print(sum(ll))

