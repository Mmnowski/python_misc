def recall_password(cipher_grille, ciphered_password):
    password = ''
    length = len(cipher_grille)
    for n in range(length):
        for m in range(length):
            if cipher_grille[n][m] == 'X':
                password += ciphered_password[n][m]
    for n in range(length):
        for m in range(length-1, -1, -1):
            if cipher_grille[m][n] == 'X':
                password += ciphered_password[n][length - 1 - m]
    for n in range(length-1, -1, -1):
        for m in range(length-1, -1, -1):
            if cipher_grille[n][m] == 'X':
                password += ciphered_password[length - 1 - n][length - 1 - m]
    for n in range(length-1, -1, -1):
        for m in range(length):
            if cipher_grille[m][n] == 'X':
                password += ciphered_password[length - 1 - n][m]
    print(password)
    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
