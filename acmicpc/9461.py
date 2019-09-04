
import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())

    arr = [1, 1, 1, 2, 2]
    if n <= 4:
        print(arr[n - 1])
    else:
        for j in range(5, n + 1):
            arr.append(arr[j - 1] + arr[j - 5])
        print(arr[n - 1])

"""
1, 1, 1, 2, 2, 3, 4, 5, 7, 9
"""
