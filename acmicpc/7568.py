
import sys

def f(l):
    return l[1]

N = int(sys.stdin.readline())

l = list()

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    l.append([i, x, y, -1])



print(l)

s1 = sorted(l, key=lambda l: -l[2])
print(s1)
s2 = sorted(l, key=lambda l: -l[1])
print(s2)

rank = 1
for i in range(len(l) - 1):

    if s1[i + 1][1] < s1[i][1] and s1[i + 1][2] < s2[i][2]:
        s1[i][3] = rank
        print('test T1', s1[i][1], s2[i][2])

        rank += 1

print(s1)
