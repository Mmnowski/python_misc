def time_converter(time):
    time_string = time[:5]
    if time_string[4] == ' ':
        time_string = time_string[:-1]
    hours, minutes = time_string.split(':')
    if time[-4] == 'p':
        if int(hours) < 12:
            hours = str(int(hours) + 12)
    else:
        if int(hours) == 12:
            hours = '00'
    # print(hours, minutes)
    # print('{}:{}'.format(hours.zfill(2), minutes))
    return '{}:{}'.format(hours.zfill(2), minutes)


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
