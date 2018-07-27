class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.corner_SE = [south, west + width_WE]
        self.corner_NE = [south + width_NS, west + width_WE]
        self.corner_NW = [south + width_NS, west]
        self.corner_SW = [south, west]
        self.width_x = width_WE
        self.width_y = width_NS
        self.height = height

    def corners(self):
        return {'north-west': self.corner_NW, 'north-east': self.corner_NE, 'south-west': self.corner_SW, 'south-east': self.corner_SE}

    def area(self):
        return self.width_x*self.width_y

    def volume(self):
        return self.area()*self.height

    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(self.corner_SW[0], self.corner_SW[1], self.width_x, self.width_y, self.height)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
