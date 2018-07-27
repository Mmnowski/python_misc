from string import ascii_uppercase


def from_camel_case(name):
    ret_value = ''
    for n in range(len(name)):
        if name[n] in ascii_uppercase and n > 0:
            ret_value += '_'
        ret_value += name[n].lower()
    return ret_value


print(from_camel_case('IAmATestString'))
