def subnetworks(net, crushes):
    working_nodes = []
    connection_ends = []
    subnet_counter = []
    for key, value in net:
        connection_ends.append(key)
    for key, value in net:
        guard = 0
        for crush in crushes:
            if crush == key:
                guard = 1
                break
        if guard == 0:
            working_nodes.append([key, value])
        else:
            if value not in connection_ends and value not in crushes:
                working_nodes.append([value, 'none'])
    print(working_nodes)
    staring_points = []
    end_points = []
    for node in working_nodes:
        staring_points.append(node[0])
        end_points.append(node[1])
    for point in staring_points:
        if point not in end_points and point not in subnet_counter:
            subnet_counter.append(point)
    print(len(subnet_counter))
    return len(subnet_counter)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, "First"
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, "Second"
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
