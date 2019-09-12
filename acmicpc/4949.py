
import sys
import re

def is_ok(s):

    l = []
    for c in s:

        if c == '(' or c == '[':
            l.append(c)
        elif c == ')':
            if len(l) <= 0:
                return False
            if l[-1] == '(':
                l.pop()
            else:
                return False
        elif c == ']':
            if len(l) <= 0:
                return False
            if l[-1] == '[':
                l.pop()
            else:
                return False
        print(l)

    if len(l) == 0:
        return True
    else:
        return False

while True:
    line = str(sys.stdin.readline())
    if 0 < len(line):
        line = line[:-1]
    else:
        break
    if line == "":
        break

    line = re.findall('[()\[\]]+', line)
    line2 = ""
    for i in line:
        line2 += i

    print('list2', line2)
    ret = is_ok(line2)
    if ret == True:
        print('yes')
    else:
        print('no')
