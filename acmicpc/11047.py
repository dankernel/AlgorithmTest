
import sys

N, price = map(int, sys.stdin.readline().split())

l = []
for i in range(N):
    l.insert(0, int(sys.stdin.readline()))

ret = 0
for coin in l:
    while price >= coin:
        ret += int(price/coin)
        price = int(price%coin)

print(ret)
