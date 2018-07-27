from typing import List
from math import sqrt, acos, degrees


def checkio(a: int, b: int, c: int) -> List[int]:
    if a == b == c:
        return [60, 60, 60]
    # elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    #     return [30, 60, 90]
    elif a + b <= c or a + c <= b or c + b <= a:
        return[0, 0, 0]
    else:
        angle_a = degrees(acos((b**2+c**2-a**2)/(2*b*c)))
        angle_b = degrees(acos((a**2+c**2-b**2)/(2*a*c)))
        angle_c = 180 - angle_a - angle_b
    values = [int(round(angle_a, 0)), int(round(angle_b, 0)), int(round(angle_c, 0))]
    return sorted(values)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
