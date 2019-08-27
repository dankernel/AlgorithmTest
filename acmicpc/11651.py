
import sys

def f(i):
    return int(i[1]), int(i[0])

n = int(sys.stdin.readline())

points = [[0 for i in range(2)] for j in range(n)]

for i in range(n):

    x, y = sys.stdin.readline().split()
    points[i][0] = x
    points[i][1] = y

sorted_points = sorted(points, key=f)

for i in sorted_points:
    print(i[0], i[1])
