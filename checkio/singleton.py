class Capital:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Capital.__instance is None:
            Capital()
        return Capital.__instance

    def __init__(self, arg):
        """ Virtually private constructor. """
        if Capital.__instance is None:
            raise Exception("This class is a singleton!")
        else:
            Capital.__instance = self
            self.name = arg

    def name(self):
        return self.name


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
