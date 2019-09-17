
import sys

N = int(sys.stdin.readline())

inputs = []
for i in range(N):
    inputs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    inputs[i][0] += min(inputs[i-1][1], inputs[i-1][2])
    inputs[i][1] += min(inputs[i-1][0], inputs[i-1][2])
    inputs[i][2] += min(inputs[i-1][0], inputs[i-1][1])
    
print(min(inputs[-1]))

