
import sys
import math

X = int(sys.stdin.readline())

root = (-1 + math.sqrt(1 + 8 * X)) / 2
root = math.ceil(root)

sig = (root * (root + 1)) / 2
sub = sig - X

x = root - sub
y = root + 1 - x

if int(x + y) % 2 == 1:
    x, y = y, x

print(int(y), end='')
print('/', end='')
print(int(x), end='')

