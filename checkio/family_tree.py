def is_family(tree):
    fathers_list = {}
    sons_list = []
    for father, son in tree:
        if father not in fathers_list.keys():
            fathers_list[father] = [son]
        else:
            fathers_list[father] += [son]
        sons_list.append(son)
    for son in sons_list:
        if son in fathers_list.keys():
            father_of_father = [i_father for i_father, i_son in tree if i_son == son][0]
            if father_of_father in fathers_list[son]:
                return False
            for child_of_father in fathers_list[son]:
                if child_of_father in fathers_list[father_of_father]:
                    return False
    if len(fathers_list.keys()) > 1:
        for father, children in fathers_list.items():
            guard = 0
            if father not in sons_list:
                for child in children:
                    if child not in fathers_list.keys():
                        guard += 1
                if guard == len(children):
                    return False
    return True


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) is True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) is True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) is True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) is False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) is False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) is False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
