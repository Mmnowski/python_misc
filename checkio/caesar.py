import string


def to_encrypt(text, delta) -> str:
    shifted_message = ''
    for letter in text:
        if letter in string.ascii_lowercase:
            shifted_message += string.ascii_lowercase[string.ascii_lowercase.index(letter)+delta]
        else:
            shifted_message += letter
    return shifted_message
