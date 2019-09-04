
import sys

max_num = 0
max_index = 0
for i in range(9):
    temp = int(sys.stdin.readline())

    if max_num < temp:
        max_num = temp
        max_index = i

print(max_num)
print(max_index + 1)
