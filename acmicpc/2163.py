
import sys

N, M = map(int, sys.stdin.readline().split())

if N < M:
    N, M = M, N

print((M-1) * N + (N-1))
