
import sys

def is_VPS(s):
    q = []

    for c in s:
        if c == '(':
            q.append('1')
        elif c == ')':
            if len(q) < 1:
                return False
            else:
                del q[-1]

    if len(q) == 0:
        return True
    else:
        return False

T = int(sys.stdin.readline())

for i in range(T):
    inputs = str(sys.stdin.readline())
    ret = is_VPS(inputs)
    if ret == True:
        print('YES')
    else:
        print('NO')


