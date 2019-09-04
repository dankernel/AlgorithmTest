
import sys

string = str(sys.stdin.readline())

freq = [-1] * 26

for c in range(len(string) - 1):
    index = ord(string[c]) - ord('a')
    if freq[index] == -1:
        freq[index] = c

for i in freq:
    print(i, end=' ')
print('\n', end='')
