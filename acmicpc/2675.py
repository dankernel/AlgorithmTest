
import sys

N = int(sys.stdin.readline())

rows = []
for i in range(N):
    R, S = sys.stdin.readline().split()
    R = int(R)
    S = str(S)

    for j in S:
        for k in range(R):
            print(j, end='')
    print("")


