TRIANGULAR_NUMBERS = []


def calc_tr_nums(limit):
    number = 1
    while number*(number+1)//2 < limit:
        TRIANGULAR_NUMBERS.append(number*(number+1)//2)
        number += 1


def checkio(number):
    global TRIANGULAR_NUMBERS
    TRIANGULAR_NUMBERS = []
    calc_tr_nums(number)
    print(TRIANGULAR_NUMBERS)
    max_list_nums = []
    max_length = 0
    num_index = len(TRIANGULAR_NUMBERS)-1
    for length in range(num_index, 1, -1):
        sum_nums = 0
        list_nums = []
        index = length
        while sum_nums <= number:
            sum_nums += TRIANGULAR_NUMBERS[index]
            list_nums.append(TRIANGULAR_NUMBERS[index])
            index -= 1
            if sum_nums == number:
                if len(list_nums) > max_length:
                    max_list_nums = list_nums
                    max_length = len(list_nums)
                break
    print(max_list_nums)
    return sorted(max_list_nums)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(994) == [], "1st example"
