import datetime
DAYS = ['Monday', 'Tuesday', "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def friday(dt):
    day, month, year = (int(x) for x in dt.split('.'))
    ans = datetime.date(year, month, day)
    if DAYS.index(ans.strftime("%A")) > DAYS.index("Friday"):
        return 7 - (2 - 7 % DAYS.index(ans.strftime("%A")))
    elif DAYS.index(ans.strftime("%A")) == DAYS.index("Friday"):
        return 0
    else:
        return DAYS.index("Friday") - DAYS.index(ans.strftime("%A"))


if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
