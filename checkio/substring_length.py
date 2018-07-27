def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    max_length = 0
    if len(line) == 0 or len(line) == 1:
        return 0
    if len(line) == 2:
        if line[0] == line[1]:
            return 1
        else:
            return 0
    for str_length in range(1, len(line)):
        str_length += 1
        for str_position in range(len(line) - str_length):
            if line.count(line[str_position:str_position + str_length]) > 1:
                max_length = len(line[str_position:str_position + str_length])
    return max_length


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('aa') == 1, "aa"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
