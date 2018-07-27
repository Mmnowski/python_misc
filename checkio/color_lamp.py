class Lamp:
    def __init__(self):
        self.colors = ['Green', 'Red', 'Blue', 'Yellow']
        self.color = ''
        self.index = -1

    def light(self):
        if self.index == -1:
            self.color = self.colors[0]
            self.index = 0
        else:
            self.index += 1
            if self.index > len(self.colors)-1:
                self.index = 0
            self.color = self.colors[self.index]
        return self.color


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
