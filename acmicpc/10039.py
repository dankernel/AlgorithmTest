
import sys

l = []
for i in range(5):
    temp = int(sys.stdin.readline())
    if 40 <= temp:
        l.append(temp)
    else:
        l.append(40)

print(int(sum(l)/5))

