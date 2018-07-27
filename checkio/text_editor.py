class Text:
    def __init__(self):
        self.text = ''
        self.message = ''
        self.font = ''

    def write(self, text):
        self.text += text
        if self.font:
            self.message = "[{}]{}[{}]".format(self.font, self.text, self.font)
        else:
            self.message = self.text

    def set_font(self, font):
        self.font = font
        self.message = "[{}]{}[{}]".format(self.font, self.text, self.font)

    def restore(self, version):
        self.text = str(version)
        self.message = str(version)

    def show(self):
        return self.message


class SavedText:
    def __init__(self):
        self.versions = {}
        self.counter = 0

    def save_text(self, Text):
        self.versions[self.counter] = Text.message
        self.counter += 1

    def get_version(self, number):
        return self.versions[number]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
