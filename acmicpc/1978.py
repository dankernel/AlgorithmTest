
import sys


def is_prime(num):

    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

N = int(sys.stdin.readline())

inputs = list(map(int, sys.stdin.readline().split()))

count = 0 
for i in inputs:
    count += is_prime(i)

print(count)
