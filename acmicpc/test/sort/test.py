l = ["apple", "ape", "banana", "bare"]

def func(item):
    return item.lower(), len(item)
print(sorted(l))
l = sorted(l, key=func)
print(l)
