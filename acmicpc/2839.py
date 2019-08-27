
import sys

ret = 0

S = int(sys.stdin.readline())

pack3k_max, mod = divmod(S, 3)
if 0 < mod:
    pack3k_max += 1
pack5k_max, mod = divmod(S, 5)
if 0 < mod:
    pack5k_max += 1

is_fail = True
min_packs = max(pack3k_max, pack5k_max) + 1
for i3 in range(pack3k_max + 1):
    for i5 in range(pack5k_max + 1):
        if (i3 * 3) + (i5 * 5) == S:
            if i3 + i5 < min_packs :
                min_packs = i3 + i5
                is_fail = False

if is_fail == True:
    print(-1)
else:
    print(min_packs)

            


"""
3x + 5y = S

x < S / 3
y < S / 5
    
"""
