
import sys

def s2(l):
    return l[1]

def s3(l):
    return l[0]

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

A = []
for i in range(len(a)):
    A.append([i, a[i], 0])

A = sorted(A, key=s2)

for i in range(len(A)):
    A[i][2] = i

A = sorted(A, key=s3)

for i in range(len(A)):
    print(A[i][2], end=' ')


