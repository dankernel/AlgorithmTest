
import sys

inputs = list(map(int, sys.stdin.readline().split()))

asc = sorted(inputs)
des = sorted(inputs, reverse=True)


if inputs == asc:
    print("ascending")
elif inputs == des:
    print("descending")
else:
    print("mixed")

