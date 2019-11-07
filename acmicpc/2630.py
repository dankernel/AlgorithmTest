
import sys
import math

boxB = 0
boxW = 0
 
def list2mat(l):

    n = int(math.sqrt(len(l)))

    mat = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(l[i * n + j])
        mat.append(row)

    return mat


def splitQ(mat):

    n = len(mat[0]) 
    h = int(n/2)

    if h < 1:
        return

    q1 = list()
    q2 = list()
    q3 = list()
    q4 = list()
    q = [q1, q2, q3, q4]
    for i in range(n):
        for j in range(n):

            if i < h and j < h:
                q1.append(mat[i][j])
            elif i < h and j >= h:
                q2.append(mat[i][j])
            elif i >= h and j < h:
                q3.append(mat[i][j])
            elif i >= h and j >= h:
                q4.append(mat[i][j])


    for qx in q:
        if sum(qx) == len(qx):
            global boxB
            boxB += 1
        elif sum(qx) == 0:
            global boxW
            boxW += 1
        else:
            splitQ(list2mat(qx))


N = int(sys.stdin.readline())

mat = list()
for i in range(N):

    row = list(map(int, sys.stdin.readline().split()))
    mat.append(row)

splitQ(mat)

print(boxW)
print(boxB)
