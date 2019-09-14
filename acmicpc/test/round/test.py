
def _round(a):
    if int(a) % 2 == 0:
        return round(a) + 1
    else:
        return round(a)

print(_round(2.5))
print(_round(3.5))
print(_round(4.5))
print(_round(5.5))

