
import sys

N = int(sys.stdin.readline())

queue = []
for i in range(N):
    inputs = list(map(str, sys.stdin.readline().split()))

    if inputs[0] == 'push':
        queue.insert(0, inputs[1])
    elif inputs[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            ret = queue.pop()
            print(ret)
    elif inputs[0] == 'size':
        print(len(queue))
    elif inputs[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inputs[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif inputs[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

