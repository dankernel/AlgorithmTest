
import sys

TC = int(sys.stdin.readline())

def runPrint(l, l2):

    maxPriority = max(l)
    if maxPriority <= l[-1]:
        # Print!

        if l2[-1] == 1:
            print('return', 1)
            return l, 1

        del l[-1]
        del l2[-1]
    else:
        # No Print!
        temp = l[-1]
        temp2 = l2[-1]
        del l[-1]
        del l2[-1]
        l.insert(0, temp)
        l2.insert(0, temp2)

    return l, 0

for i in range(TC):

    N, M = map(int, sys.stdin.readline().split())

    l = list(map(int, sys.stdin.readline().split()))
    print('> list0 :', l)
    l2 = [0] * N
    l2[M] = 1

    count = 1
    while 0 < len(l):

        print('> list1 :', l, count)
        print('> list2 :', l2, count)

        _, ret = runPrint(l, l2)
        if ret == 1:
            print('return 1..')
            print(count)
            break
            
        count += 1

    print('count :', count)


