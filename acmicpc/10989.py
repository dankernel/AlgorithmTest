
import operator
import sys

n = int(sys.stdin.readline())

freq = [0] * 10001
for i in range(n):
    temp = int(sys.stdin.readline())
    freq[temp] += 1

for i in range(10001):
    for j in range(freq[i]):
        print(i)

