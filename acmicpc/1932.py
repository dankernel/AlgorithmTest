
import sys

n = int(sys.stdin.readline())

inputs = []
for i in range(n):
    inputs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            a = 0
        else:
            a = inputs[i-1][j-1]
        if i == j:
            b = 0
        else:
            b = inputs[i-1][j]
        inputs[i][j] += max(a, b)

print(max(inputs[-1]))
