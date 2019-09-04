
import sys

def get_prime_list(num):

    table = [True] * (num + 1)
    table[0] = False
    table[1] = False

    for i in range(2, num + 1):
        if table[i] == True:
            for j in range(2, (num)//i + 1):
                table[i * j] = False

    return table

M, N = map(int, sys.stdin.readline().split())

ret = get_prime_list(N)
for i in range(M, len(ret)):
    if ret[i] == True:
        print(i)
