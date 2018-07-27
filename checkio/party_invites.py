class Friend:
    def __init__(self, name):
        self.name = name
        self.invites = []

    def add_invite(self, invite):
        self.invites.append(invite)

    def show_invite(self):
        if self.invites:
            return self.invites.pop()
        else:
            return 'No party...'


class Party:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_friend(self, friend):
        self.members.append(friend)

    def del_friend(self, friend):
        self.members.remove(friend)

    def send_invites(self, message):
        for member in self.members:
            member.add_invite('{}: {}'.format(self.name, message))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
