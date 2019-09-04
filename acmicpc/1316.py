
import sys

N = int(sys.stdin.readline())

inputs = []
for i in range(N):
    inputs.append(str(sys.stdin.readline())[:-1])

for string in inputs:
    print(string)

