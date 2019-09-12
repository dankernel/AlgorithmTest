
import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()

for i in range(1, N+1):
    q.append(i)

while 1 < len(q):
    q.popleft()
    q.append(q.popleft())

    if len(q) <= 1:
        break

print(q[0])
