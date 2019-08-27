
import sys

n = int(sys.stdin.readline())

inputs = []
for i in range(n):
    inputs.append(int(sys.stdin.readline()))

inputs.sort()

for i in inputs:
    print(i)
