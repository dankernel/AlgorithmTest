
import sys

K = int(sys.stdin.readline())

inputs = []
for i in range(K):
    temp = int(sys.stdin.readline())

    if temp == 0 and 0 < len(inputs):
        del inputs[-1]
    else:
        inputs.append(temp)

print(sum(inputs))
