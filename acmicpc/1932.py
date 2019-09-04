
import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append([])
    arr[i] = list(map(int, (sys.stdin.readline().split())))

index = 0
ret = 0
for i in range(1, n):

    if arr[i][index] < arr[i][index + 1] :
        ret += arr[i][index + 1] 
        print(arr[i][index + 1])
        index += 1
    elif arr[i][index] > arr[i][index + 1] :
        print(arr[i][index])
        ret += arr[i][index] 
    
print(arr)
print(ret)


"""

0
00
000
0000

"""
