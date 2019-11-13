
import sys

t = int(sys.stdin.readline())
for i in range(t):

    N = int(sys.stdin.readline())

    l = []
    for j in range(N):
        l.append(str(sys.stdin.readline())[:-2].rstrip())
    l.sort()

    print(l)

    ret = 0
    for i in range(len(l) - 1):
        if len(l[i]) < len(l[i+1]):
            if l[i+1][:len(l[i])] == l[i][:len(l[i])]:
                ret = 1
                break

    if ret == 1:
        print('NO')
    else:
        print('YES')

