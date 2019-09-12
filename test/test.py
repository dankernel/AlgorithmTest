
import sys
import time

start = time.time()  
rl = sys.stdin.readline()
for i in range(1000000):
    temp = int(rl)

print("time :", time.time() - start) 
