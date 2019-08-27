
import sys

def f(i):
    return int(i[0]), int(i[2])

n = int(sys.stdin.readline())

users = [[0 for i in range(3)] for j in range(n)]

for i in range(n):
    age, name = sys.stdin.readline().split()
    users[i][0] = age
    users[i][1] = name
    users[i][2] = i

sorted_users = sorted(users, key=f)

for i in sorted_users:
    print(i[0], i[1])


