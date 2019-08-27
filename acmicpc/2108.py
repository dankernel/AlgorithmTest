# Input
import collections
import math
import sys

def _round(a):
    if int(a) % 2 == 0:
        return round(a) + 1
    else:
        return round(a)

n = int(sys.stdin.readline())
inputs = []

for i in range(n):
    temp = int(sys.stdin.readline())
    inputs.append(temp)

# Sort
inputs.sort()

out_max = max(inputs)
out_min = min(inputs)
out_sum = sum(inputs)

# 1
out_avg = out_sum / len(inputs)
print(round(out_avg))

# 2
size = len(inputs) 
median = inputs[size//2]
print(median)

# 3
c = collections.Counter(inputs)
c = c.most_common()

if len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

# 4
print(out_max - out_min)
