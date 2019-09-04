
import sys

N = int(sys.stdin.readline())

for i in range(N):
    score = list(map(int, sys.stdin.readline().split()[1:]))

    ave = sum(score) / len(score)
    over_score = 0
    for j in score:
        if ave < j:
            over_score += 1

    print("%.3f"%round(over_score / len(score) * 100, 3), end='')
    print('%')
