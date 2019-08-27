
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())


print(A * int(str(B)[-1]))
print(A * int(str(B)[-2]))
print(A * int(str(B)[-3]))
print(A * B)
