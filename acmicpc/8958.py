
import sys

N = int(sys.stdin.readline())

inputs = []
for i in range(N):
    temp = str(sys.stdin.readline()[:-1])
    inputs.append(temp)

    ret = 0
    score = 0
    for x in temp:
        if x == 'O':
            score += 1
            ret += score
        else:
            score = 0

    print(ret)

