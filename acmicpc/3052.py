
import sys

table = [0] * 42
for i in range(10):
    temp = int(sys.stdin.readline())

    table[temp % 42] += 1

sum_val = 0
for i in table:
    if 0 < i:
        sum_val += 1

print(sum_val)


    
