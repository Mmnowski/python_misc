def checkio(int_list):
    occurences = {}
    for n in int_list:
        if occurences.get(n):
            occurences[n] += 1
        else:
            occurences[n] = 1
    for key, value in occurences.items():
        if value == 1:
            int_list.remove(key)
    return int_list


print(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
# checkio([1, 2, 3, 4, 5]) == []
# checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
# checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
