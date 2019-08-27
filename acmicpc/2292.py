
import sys
import math

inputs = int(sys.stdin.readline())

if inputs == 1:
    print(1)
else:
    i = 1
    while inputs > 3 * i * (i - 1) + 1:
        i += 1
        # print(3 * i * (i - 1) + 1)

    print(i)

"""
N hexagon outline : (N - 1) * 6 , (1 < N)....

"""
