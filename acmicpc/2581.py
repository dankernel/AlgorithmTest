
import sys

def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime_list = []
for i in range(M, N + 1):
    if is_prime(i) == True:
        prime_list.append(i)

if 0 < len(prime_list):
    print(sum(prime_list))
    print(prime_list[0])
else:
    print(-1)

    

