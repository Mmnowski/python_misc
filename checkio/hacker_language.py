from string import ascii_letters


class HackerLanguage:
    def __init__(self):
        self.message = ''

    def write(self, message):
        encoded_message = ''
        for letter in message:
            if letter in ascii_letters:
                encoded_message += "{0:b}".format(ord(letter))
            elif letter == ' ':
                encoded_message += "1000000"
            else:
                encoded_message += letter
        self.message += encoded_message

    def delete(self, value):
        self.message = self.message[:-value*7]

    def send(self):
        return self.message

    def read(self, s):
        message = ''
        letter = ''
        for i in s:
            if i not in '01':
                message += i
            else:
                letter += i
            if len(letter) == 7:
                if letter != '1000000':
                    message += chr(int(letter, 2))
                    letter = ''
                else:
                    message += ' '
                    letter = ''
        return message


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
