
number_size = 10000

def d(n):
    ret = n
    num = str(n)
    for c in num:
        ret += int(c)

    return ret


table = [0] * number_size
for i in range(number_size):
    temp = d(i)
    if temp < number_size:
        table[d(i)] = 1

for i in range(len(table)):
    if table[i] == 0:
        print(i)


