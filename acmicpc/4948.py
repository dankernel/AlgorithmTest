
import sys

def f(n):
    table = [True] * (n + 1)

    table[0] = False
    table[1] = False
    for i in range(2, n + 1):
        if table[i] == True:
            for j in range(2, n//i + 1):
                table[i * j] = False

    return table

table = f(123456 * 2)
n = -1
while True:

    n = int(sys.stdin.readline())
    if n == 0:
        break

    n2 = n * 2
    s = 0
    for i in range(n + 1, n2 + 1):
        if table[i] == True:
            s += 1
    print(s)

