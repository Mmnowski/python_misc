import string


def checkio(password):
    def check_in(match_case, passw):
        flag_good = True
        for n in match_case:
            if n in passw:
                flag_good = True
                break
            else:
                flag_good = False
        return flag_good
    if check_in(string.digits, password) and check_in(string.ascii_uppercase, password) and check_in(string.ascii_lowercase, password) and len(password) >= 10:
        return True
    else:
        return False


print(checkio('A1213pokl'))
print(checkio('bAse730onE'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))
