
import sys

def f(i):
    return len(i), i

n = int(sys.stdin.readline())

words = []
for i in range(n):
    temp = str(sys.stdin.readline())
    if temp not in words:
        words.append(temp)

sorted_words = sorted(words, key=f)

for i in sorted_words:
    print(i, end='')
