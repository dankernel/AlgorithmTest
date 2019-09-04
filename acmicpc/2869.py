
import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

if V - B < 1:
    print(1)
else:
    day = (V - B) / (A - B)
    print(math.ceil(day))

"""
V = len <------------->
A = go   --->(a)
B = back  <--(b)

in N day)
A * day - (B * day + A * day) = V

case 2 1 5)
2 * day - (1 * day + 2 * day) = 5
3 * day = 5
"""
