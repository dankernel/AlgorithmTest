
import sys

def f(n):

    number = str(n)

    if len(number) < 2:
        return True

    diff = int(number[0]) - int(number[1])
    for i in range(len(number) - 1):
        if diff != int(number[i]) - int(number[i + 1]):
            return False

    return True

num = int(sys.stdin.readline())

ret = 0
for i in range(1, num + 1):
    if f(i) == True:
        ret += 1

print(ret)


