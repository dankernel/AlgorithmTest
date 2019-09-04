
import sys

mul = 1
table = [0]*10
for i in range(3):
    mul *= int(sys.stdin.readline())

mul = str(mul)
for digit in mul:
    table[int(digit)] += 1

for i in table:
    print(i)

