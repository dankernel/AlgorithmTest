
import sys

N = int(sys.stdin.readline())
temp = N
ret = 0

if temp < 10:
    temp += temp * 10
    ret += 1

    if temp == N:
        print(ret)
        exit()

digit10 = temp // 10
digit1 = temp % 10
temp = (digit1 * 10) + ((digit10 + digit1) % 10)
ret += 1
 
while temp != N:
    if temp < 10:
        temp += temp * 10
        ret += 1

        if temp == N:
            break

    digit10 = temp // 10
    digit1 = temp % 10
    temp = (digit1 * 10) + ((digit10 + digit1) % 10)
    ret += 1

print(ret)

