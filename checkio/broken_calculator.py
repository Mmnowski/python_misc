def checkio(data):
    check_sum = 0

    def add(a, b, length):
        if length > 0:
            a += b[length-1]
            length -= 1
            return add(a, b, length)
        else:
            return a
    return add(check_sum, data, len(data))
print(checkio([1, 2, 3]))
checkio([2, 2, 2, 2, 2, 2]) == 12
