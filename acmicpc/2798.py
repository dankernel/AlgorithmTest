
import sys

N, M = map(int, sys.stdin.readline().split())
Ni = list(map(int, sys.stdin.readline().split()))

ret = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:

                temp = Ni[i] + Ni[j] + Ni[k]
                if temp <= M and ret < temp:
                    ret = temp
                if ret == M:
                    break

print(ret)

