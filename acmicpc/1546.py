
import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

M = max(score)

new_score = list(map(lambda x : x/M*100, score))

ret = sum(new_score) / len(new_score)
print(ret)


