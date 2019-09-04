
import sys

A, B = map(int, sys.stdin.readline().split())

while A != 0 and B != 0:
    print(A + B)
    A, B = map(int, sys.stdin.readline().split())

