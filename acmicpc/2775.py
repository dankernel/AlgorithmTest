
import sys

T = int(sys.stdin.readline())

def init_table():
    table = []
    for k in range(15):
        table.append([])
        for b in range(15):
            if k == 0:
                table[k].append(b)
            else:
                table[k].append(sum(table[k-1][:b + 1]))

    return table

for i in range(T):
    kk = int(sys.stdin.readline())
    bb = int(sys.stdin.readline())

    table = init_table()
    print(table[kk][bb])



