import string


def safe_pawns(pawns):
    counter = 0
    elements = list(pawns)
    for n in elements:
        place = string.ascii_lowercase.find(n[0])
        elements[elements.index(n)] = n.replace(n[0], str(place+1))
    elements.sort()
    return len([n for n in elements if str(int(n) - 11) in elements or str(int(n) + 9) in elements])


print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
