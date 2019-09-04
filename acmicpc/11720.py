
import sys

N = int(sys.stdin.readline())
string = str(sys.stdin.readline())

ret = 0
for i in string[:-1]:
    ret += int(i)

print(ret)


