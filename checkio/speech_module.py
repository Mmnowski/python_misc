FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number < 10:
        return FIRST_TEN[number-1]
    elif number < 20:
        print(SECOND_TEN[number-11])
        return SECOND_TEN[number-10]
    else:
        value = ''
        ones = round((number/10 - number//10) * 10)
        tens = round((number/100 - number//100) * 100)
        print(tens)
        hundreds = int((number/1000 - number//1000) * 10)
        if hundreds > 0:
            print(hundreds)
            value += FIRST_TEN[hundreds-1] + ' hundred '
        if tens < 20 and tens > 9:
            value += SECOND_TEN[tens-10] + ' '
            return value[:-1]
        tens = tens - ones
        if tens != 0:
            value += OTHER_TENS[(tens//10)-2] + ' '
        if ones != 0:
            value += FIRST_TEN[ones-1] + ' '
    print(value)
    return value[:-1]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(999) == 'nine hundred ninety nine', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
