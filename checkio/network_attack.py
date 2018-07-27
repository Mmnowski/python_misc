# not finished, no clue how to
def capture(matrix):
    def find_path(start_node):
        return 0
    security_list = {}
    for n in range(len(matrix)):
        security_list[n] = matrix[n][n]
    connections = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                if matrix[i][j] == 1:
                    if i not in connections.keys():
                        connections[i] = [j]
                    else:
                        connections[i] += [j]
    all_times = {}
    for values in connections[0]:
        find_path
    print(security_list, connections)
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
