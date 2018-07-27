def checkio(data):
    value = ''
    while True:
        if data//1000 > 0:
            data -= 1000
            value += 'M'
        elif data//100 == 9:
            data -= 900
            value += 'CM'
        elif data//500 > 0:
            data -= 500
            value += 'D'
        elif data//100 > 3:
            data -= 400
            value += 'CD'
        elif data//100 > 0:
            data -= 100
            value += 'C'
        elif data//10 == 9:
            data -= 90
            value += 'XC'
        elif data//50 > 0:
            data -= 50
            value += 'L'
        elif data//10 > 3:
            data -= 40
            value += 'XL'
        elif data//10 > 0:
            data -= 10
            value += 'X'
        elif data//1 == 9:
            data -= 9
            value += 'IX'
        elif data//5 > 0:
            data -= 5
            value += 'V'
        elif data//1 > 3:
            data -= 400
            value += 'IV'
        elif data//1 > 0:
            data -= 1
            value += 'I'
        else:
            break
    return value


print(checkio(6))
print(checkio(76))
print(checkio(499))
print(checkio(3888))
print(checkio(3000))
