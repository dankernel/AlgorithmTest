
def convert(n:int, base:int) -> str:
    """
    n : Number
    base : digit
    """
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def add_digit(number, digits):
    """
    Add each digit
    number : str
    """
    return sum([int(i, digits) for i in str(number)])

for i in range(1000, 9999):
    # Sum each digit
    sum_x10 = add_digit(convert(i, 10), 10)
    sum_x12 = add_digit(convert(i, 12), 12)
    sum_x16 = add_digit(convert(i, 16), 16)

    # Same all.
    if sum_x10 == sum_x12 == sum_x16 :
        print(i)
