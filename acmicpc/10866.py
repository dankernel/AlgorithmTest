
import sys

N = int(sys.stdin.readline())

l = list()
for i in range(N):
    
    com = list(map(str, sys.stdin.readline().split()))

    if com[0] == 'push_front':
        l.insert(0, com[1])
    if com[0] == 'push_back':
        l.insert(len(l), com[1])
    if com[0] == 'pop_front':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
            del l[0]
    if com[0] == 'pop_back':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])
            del l[-1]
    if com[0] == 'size':
        print(len(l))
    if com[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    if com[0] == 'front':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
    if com[0] == 'back':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])


