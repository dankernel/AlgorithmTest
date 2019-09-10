
import sys

def DFS(g, index):
    stack = []
    used = []

    while True:
        # Add child to stack
        for i in range(len(g[index])):
            if g[index][i] not in used:
                stack.append(g[index][i])

        if index not in used:
            print(index, end=' ')
            used.append(index)
        if len(stack) <= 0:
            return
        
        index = stack.pop()

def BFS(g, index):

    queue = []
    used = []

    while True:
        for i in range(len((g[index]))):
            if g[index][i] not in used:
                queue.insert(0, g[index][i])

        if index not in used:
            print(index, end=' ')
            used.append(index)
        if len(queue) <= 0:
            return

        index = queue.pop()

N, M, V = map(int, sys.stdin.readline().split())

# Inputs
g = [[] for i in range(N + 1)]
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    g[n1].append(n2)
    g[n2].append(n1)

# DFS
for i in range(N + 1):
    if 0 < len(g[i]):
        g[i].sort(reverse=True)
DFS(g.copy(), V)
print()

# BFS
for i in range(N + 1):
    if 0 < len(g[i]):
        g[i].sort()
BFS(g.copy(), V)
print()
