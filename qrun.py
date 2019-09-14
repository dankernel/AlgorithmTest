#!/usr/bin/env python

import os

# Open fd and config file
try:
    f_config = open('.qconfig', 'r')
    f_output = open('output', 'r')
    f_result = open('result', 'r')
    qnum = f_config.readline()
except:
    print('[FAIL] No file')

# Run 
try:
    run = 'python q' + qnum + '.py < input > result'
    os.system(run)
except:
    print('[FAIL] Run error')

# Check result/output
while True:
    ol = f_output.readline()
    rl = f_result.readline()

    if ol != rl :
        print('[FAIL]')
        break
    
    if not ol or not rl:
        print('[OK] PASS')
        break

f_config.close()
f_output.close()
f_result.close()

