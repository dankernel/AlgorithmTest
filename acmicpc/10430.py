
import sys

inputs = []
inputs = list(map(int, sys.stdin.readline().split()))

A = inputs[0]
B = inputs[1]
C = inputs[2]


print((A+B)%C)
print((A%C + B%C)%C)
print((A*B)%C)
print((A%C * B%C)%C)

