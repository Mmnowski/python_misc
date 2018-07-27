def checkio(histogram):
    max_val = len(histogram)
    if max_val == 1:
        return max_val if max_val > histogram[0] else histogram[0]
    for n in range(len(histogram)-1):
        height = histogram[n]
        if height > max_val:
            max_val = height
        for m in range(n, len(histogram)-1):
            if height > histogram[m+1]:
                height = histogram[m+1]
            if height > 1:
                if height*(m-n+2) > max_val:
                    max_val = height*(m-n+2)
            else:
                break
    return max_val


print(checkio([2, 1, 4, 5, 1, 3, 3]))
