f = open('input', 'r')

n = int(f.readline())
inputs = {}
for i in range(n):
    text = f.readline()
    l = len(text) 
    if l not in inputs:
        inputs[l] = []
    inputs[l].append(text)

sorted_keys = sorted(inputs.keys())

for key in sorted_keys:
    remove_dep = sorted(list(set(inputs[key])))
    for i in remove_dep:
        print(i)
