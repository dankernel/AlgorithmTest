
import sys

nums = list(map(int, sys.stdin.readline().split()))

nums[0] = int(str(nums[0])[::-1])
nums[1] = int(str(nums[1])[::-1])

if nums[0] < nums[1] :
    print(nums[1])
else :
    print(nums[0])



