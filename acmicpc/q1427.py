
import sys

inputs = str(sys.stdin.readline())

splited_list = []
for i in range(len(inputs) - 1) :
    splited_list.append(inputs[i])

splited_list.sort(reverse=True)

for i in range(len(inputs)-1):
    print(splited_list[i], end='')
