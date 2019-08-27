
import sys

A, B = sys.stdin.readline().split()


if int(A) < int(B):
    print('<')
elif int(A) > int(B):
    print('>')
elif int(A) == int(B):
    print('==')
