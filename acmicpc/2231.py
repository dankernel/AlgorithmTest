
import sys


def sumdig(n):
    ret = 0
    for i in n:
        ret = ret + int(i)

    return ret

N = int(sys.stdin.readline())

if N < 10:
    print(0)
    exit()

l = len(str(N))

start = l
end = l * 9

ret = 0
for i in range(start, end):

    initer = N - i
    sumdigit = sumdig(str(N - i))

    if initer + sumdigit == N:
        ret = initer

print(ret)


