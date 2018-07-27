def checkio(n, m):
    counter = 0
    binary_1 = "{0:b}".format(n)
    binary_2 = "{0:b}".format(m)
    if len(binary_1) < len(binary_2):
        binary_1, binary_2 = binary_2, binary_1
    binary_2 = binary_2.zfill(len(binary_1))
    for n in range(len(binary_1)):
        print(n, binary_1, binary_2, binary_1[n], binary_2[n])
        if int(binary_1[n]) + int(binary_2[n]) == 1:
            counter += 1
    return counter


print(checkio(117, 17))
