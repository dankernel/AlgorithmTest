
import sys

inputs = str(sys.stdin.readline())
print(inputs)

count = 0
mapp_talbe = [['č', 'c='],
        ['ć', 'c-'],
        ['d', 'dz='],
        ['đ', 'd-'],
        ['lj', 'lj'],
        ['nj', 'nj'],
        ['š', 's='],
        ['ž', 'z=]']]

print(mapp_talbe)

for i in range(10):
    for j in mapp_talbe:
        temp = inputs.replace(j[1], j[0])
        
        if inputs != temp:
            count += 1
            inputs = temp

print(inputs)
print(count)
