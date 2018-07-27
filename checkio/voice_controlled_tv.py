class VoiceCommand:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.is_channel = self.channel_list[0]

    def current_channel(self):
        return self.is_channel

    def set_channel(self, channel):
        self.is_channel = channel

    def first_channel(self):
        self.set_channel(self.channel_list[0])
        return self.current_channel()

    def last_channel(self):
        self.set_channel(self.channel_list[-1])
        return self.current_channel()

    def turn_channel(self, num):
        self.set_channel(self.channel_list[num-1])
        return self.current_channel()

    def next_channel(self):
        index = self.channel_list.index(self.current_channel())+1 if self.channel_list.index(self.current_channel()) + \
            1 < len(self.channel_list) else self.channel_list.index(self.current_channel())+1 - len(self.channel_list)
        self.set_channel(self.channel_list[index])
        return self.current_channel()

    def previous_channel(self):
        index = self.channel_list.index(self.current_channel())-1 if self.channel_list.index(self.current_channel()) - \
            1 >= 0 else self.channel_list.index(self.current_channel())-1 + len(self.channel_list)
        self.set_channel(self.channel_list[index])
        return self.current_channel()

    def is_exist(self, var):
        if type(var) == int:
            return "Yes" if var < len(self.channel_list) else "No"
        elif type(var) == str:
            return "Yes" if var in self.channel_list else "No"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
