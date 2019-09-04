
import sys

H, M = map(int, sys.stdin.readline().split())

if M < 45:
    H -= 1
    M += 60

    if H < 0:
        H = 23

M -= 45

print(H, M)
