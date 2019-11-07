
import sys

N = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))
print(l)
print(*l)

for i in range(N):
    pic = l[0]
    del l[0]

    ret = -1
    for j in l:
        if pic <= j:
            ret = j
            break

    print(ret, end=' ')


    



