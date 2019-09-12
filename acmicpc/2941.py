
import sys
import re

inputs = str(sys.stdin.readline())[:-1]

count = 0
ret = re.findall('c=|c-|dz=|d-|lj|nj|s=|z=', inputs)
count += len(ret)
for i in ret:
    inputs = inputs.replace(i, '', 1)

count += len(inputs)
print(count)

