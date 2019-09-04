
import sys

def f(i):
    return -i[1]

inputs = str(sys.stdin.readline())
inputs = inputs.lower()

freq = [[0 for i in range(2)] for j in range(26)]
for i in range(len(freq)):
    freq[i][0] = i

for i in inputs[:-1]:
    freq[ord(i) - ord('a')][1] += 1

freq = sorted(freq, key=f)
if freq[0][1] == freq[1][1]:
    print('?')
else:
    print(chr(ord('A') + freq[0][0]))
