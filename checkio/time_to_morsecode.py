def checkio(time_string: str) -> str:
    def time_to_binary(num, flag):
        if flag == 0:
            binary = "{0:02b}".format(int(num))
        elif flag == 1:
            binary = "{0:04b}".format(int(digit))
        elif flag == 2:
            binary = "{0:03b}".format(int(digit))
        elif flag == 3:
            binary = "{0:04b}".format(int(digit))
        elif flag == 4:
            binary = "{0:03b}".format(int(digit))
        elif flag == 5:
            binary = "{0:04b}".format(int(digit))
        return binary

    morse_code = ''
    time = time_string.split(':')
    counter = 0
    for number in time:
        if len(number) != 2:
            number = number.zfill(2)
        for digit in number:
            binary = time_to_binary(digit, counter)
            counter += 1
            for bit in binary:
                if bit == '0':
                    morse_code += '.'
                else:
                    morse_code += '-'
            morse_code += ' '
        morse_code += ': '
    return morse_code[:-3]


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
