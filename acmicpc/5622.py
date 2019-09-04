
import sys

times = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

inputs = str(sys.stdin.readline())

ret = 0
for i in inputs[:-1]:
    index = ord(i) - ord('A')
    ret += times[index]

print(ret)

