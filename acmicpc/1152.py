
import sys

inputs = str(sys.stdin.readline())

ret = 0
for i in inputs[:-1]:
    if i == ' ':
        ret += 1

if inputs[0] == ' ':
    ret -= 1
if inputs[-2] == ' ':
    ret -= 1

print(ret + 1)

