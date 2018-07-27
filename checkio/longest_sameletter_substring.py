def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    max_len = 0
    while len(line) > 0:
        len_pre = len(line)
        letter = line[0]
        for n in line:
            if letter == n:
                line = line[1:]
                print(line)
            else:
                break
        len_post = len(line)
        if len_pre - len_post > max_len:
            max_len = len_pre - len_post
    return max_len


print(long_repeat('aaaaaabbbbbbcccccdddddddd'))
