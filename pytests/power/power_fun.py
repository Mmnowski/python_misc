def power(x, n):
    if x == 0 and n == 0:
        return "Nope"
    if x < 1:
        return 0
    if n < 1 and n > 0:
        return "Nope"
    if n == 0:
        return 1

    return x**n
