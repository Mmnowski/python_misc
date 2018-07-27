class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        values = set()
        for key, val in self.connections:
            if key in values:
                pass
            else:
                values.add(key)
            if val in values:
                pass
            else:
                values.add(val)
        return values

    def connected(self, name):
        values = set()
        for key, val in self.connections:
            if key == name:
                values.add(val)
            elif val == name:
                values.add(key)
        return values


letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
digit_friends = Friends([{"1", "2"}, {"3", "1"}])
print(letter_friends.add({"c", "d"}))
print(letter_friends.add({"c", "d"}))
print(letter_friends.remove({"c", "d"}))
print(digit_friends.remove({"c", "d"}))
print(letter_friends.names() == {"a", "b", "c"})
print(letter_friends.connected("d") == set())
print(letter_friends.connected("a") == {"b", "c"})
