
import sys
import collections
import operator

inputs = str(sys.stdin.readline())

chars = []
for i in range(len(inputs) - 1):
    chars.append(inputs[i])

counted = collections.Counter(chars)
print(counted)
print(collections.OrderedDict(counted))


if str(counted[sorted_coint_key[0]]) == str(counted[sorted_coint_key[1]]):
    print('?')
else:
    print(counted[sorted_coint_key[0]])

