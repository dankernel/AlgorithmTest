
import sys

def sortEnd(l):
    return l[1]

# Insert data
l = []
for i in range(int(sys.stdin.readline())):
    l.append(list(map(int, sys.stdin.readline().split())))

# Sort, End, start
l = sorted(l, key=sortEnd)

meeting = 0
end = 0
for i in range(len(l)):

    l = filter(lambda x: end <= x[0], l)
    if len(l) <= 0:
        break

    l = sorted(l, key=sortEnd)
    print(l[0])

    end = l[0][1]
    
    del l[0]
    meeting += 1

print(meeting)

