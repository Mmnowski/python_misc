trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    conversion = ''
    size = len(str(us_num))
    if size > 0:
        word = str(us_num)
        for n in range(size):
            if size > 1:
                if int(us_num)//10 != 1:
                    conversion += trans[word[n]] + ' '
                conversion += trans['10'] + ' '
                size -= 1
            else:
                if int(us_num) % 10 != 0 or conversion == '':
                    conversion += trans[word[n]]
    return conversion


print(convert_to_mandarin('1'))
