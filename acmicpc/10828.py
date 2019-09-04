
import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    inputs = list(map(str, sys.stdin.readline().split()))

    if inputs[0] == 'push':
        stack.insert(0, inputs[1])
    elif inputs[0] == 'pop':
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[0])
            del stack[0]
    elif inputs[0] == 'size':
        print(len(stack))
    elif inputs[0] == 'empty':
        if len(stack) <= 0:
            print(1)
        else:
            print(0)
    elif inputs[0] == 'top':
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[0])

