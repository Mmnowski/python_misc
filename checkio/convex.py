def checkio(data):
    Matrix = [[0 for x in range(10)] for y in range(10)]
    index = 0
    for x, y in data:
        Matrix[10-][x] = index
        index += 1
    print(Matrix)
    return [0, 1, 2]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
