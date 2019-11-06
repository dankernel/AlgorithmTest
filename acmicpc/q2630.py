
import sys
import math


def list2mat(l):

    n = int(math.sqrt(len(l)))
    print(l)

    mat = list()
    for i in l:
        row = list()
        for j in range(n):
            row.append(i)
        mat.append(row)
        print(row)
    print()

    return mat


def splitQ(mat):

    n = len(mat[0]) 
    h = int(n/2)

    if h <= 1:
        return

    q1 = list()
    q2 = list()
    q3 = list()
    q4 = list()
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

    splitQ(list2mat(q1))
    splitQ(list2mat(q2))
    splitQ(list2mat(q3))
    splitQ(list2mat(q4))


N = int(sys.stdin.readline())

mat = list()
for i in range(N):

    row = list(map(int, sys.stdin.readline().split()))
    mat.append(row)

splitQ(mat)
