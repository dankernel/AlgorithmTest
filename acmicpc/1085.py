
import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))

a = w - x
b = h - y

ret = min(x, y, a, b)

print(ret)
