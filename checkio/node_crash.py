def disconnected_users(net, users, source, crushes):
    def count_users(source, connections):
        count = 0
        if source in connections.keys():
            for node in connections[source]:
                count += users[node]
                count += count_users(node, connections)
            return count
        else:
            return count
    working_nodes = []
    connections = {}
    num_users = 0
    for node in net:
        guard = 0
        for crush in crushes:
            if crush in node:
                guard = 1
                break
        if guard == 0:
            working_nodes.append(node)

    for key, value in users.items():
        for node in working_nodes:
            if key == node[0]:
                if connections.get(key, -1) != -1:
                    connections[key] += [node[1]]
                else:
                    connections[key] = [node[1]]
    if source not in crushes:
        num_users += users[source]
        num_users += count_users(source, connections)
    return sum(users.values()) - num_users


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"
    print()
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"
    print()
    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"
    print()
    print(disconnected_users([["A", "B"], ["A", "C"], ["A", "D"], ["A", "E"], ["A", "F"]],
                             {"A": 10, "C": 10, "B": 10, "E": 10, "D": 10, "F": 10}, "A", ["B", "C"]))

    print('Done. Try to check now. There are a lot of other tests')
