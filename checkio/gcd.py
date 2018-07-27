from math import pi, sqrt


def simple_areas(*args):
    list_args = list(args)
    if len(list_args) == 1:
        return round(pi/4*list_args[0]**2, 2)
    elif len(list_args) == 2:
        return list_args[0]*list_args[1]
    elif len(list_args) == 3:
        a = list_args[0]
        b = list_args[1]
        c = list_args[2]
        p = (a+b+c)/2
        return round(sqrt(p*(p-a)*(p-b)*(p-c)), 2)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
