
import sys

N = int(sys.stdin.readline())

def f(str):
    charlist = []
    prev = ""
    for c in string:
        if prev != c:
            prev = c
            if c in charlist:
                return False
            charlist.append(c)
    return True

inputs = []
for i in range(N):
    inputs.append(str(sys.stdin.readline())[:-1])

c = 0
for string in inputs:
    ret = f(string)
    if ret == True:
        c += 1

print(c)
