
import sys

N = int(sys.stdin.readline())

inputs = []
for i in range(N):
    # input reverse
    temp = int(sys.stdin.readline())
    inputs.append(temp)

s = []
s.append(inputs[0])
s.append(inputs[0] + inputs[1])
s.append(max(inputs[2] + inputs[1], inputs[0] + inputs[2]))

for i in range(3, N):
    s.append(max(inputs[i] + s[i-2], inputs[i] + inputs[i-1] + s[i-3]))

print(s[N-1])
