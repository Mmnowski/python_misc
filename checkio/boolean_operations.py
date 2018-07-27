def boolean(x, y, operation):
    if operation == 'conjunction':
        return 1 if x and y else 0
    elif operation == 'disjunction':
        return 1 if x or y else 0
    elif operation == 'disjunction':
        return 1 if (not x) or y else 0
    elif operation == 'disjunction':
        return 1 if (x or y) and not (x and y) else 0
    elif operation == 'disjunction':
        return 1 if not (x or y) and not (x and y) else 0
    else:
        return None
