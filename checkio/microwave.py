class MicrowaveBase:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0

    def set_time(self, time):
        time_split = time.split(':')
        self.minutes = int(time_split[0])
        self.seconds = int(time_split[1])

    def add_time(self, time):
        if time[-1] == 'm':
            self.seconds += int(time[:-1])*60
        else:
            self.seconds += int(time[:-1])
        count = 0
        while self.seconds >= 60:
            count += 1
            self.seconds -= 60
        self.minutes += count
        if self.minutes > 90:
            self.minutes = 90
            self.seconds = 0

    def del_time(self, time):
        if time[-1] == 's':
            self.seconds += self.minutes*60
            self.seconds -= int(time[:-1])
            self.minutes = 0
            if self.seconds < 0:
                self.seconds = 0
            elif self.seconds > 60:
                count = 0
                while self.seconds > 60:
                    count += 1
                    self.seconds -= 60
                self.minutes += count
        else:
            self.minutes -= int(time[:-1])
            if self.minutes < 0:
                self.minutes = 0
                self.seconds = 0

    def show_time(self):
        return self.time


class Microwave1(MicrowaveBase):
    def show_time(self):
        minutes = '_'
        minutes += str(self.minutes).zfill(2)[1:]
        seconds = str(self.seconds).zfill(2)
        print('{}:{}'.format(minutes, seconds))
        return '{}:{}'.format(minutes, seconds)


class Microwave2(MicrowaveBase):
    def show_time(self):
        minutes = str(self.minutes).zfill(2)
        seconds = str(self.seconds).zfill(2)[:-1]
        seconds += '_'
        print('{}:{}'.format(minutes, seconds))
        return '{}:{}'.format(minutes, seconds)


class Microwave3(MicrowaveBase):
    def show_time(self):
        minutes = str(self.minutes).zfill(2)
        seconds = str(self.seconds).zfill(2)
        print('{}:{}'.format(minutes, seconds))
        return '{}:{}'.format(minutes, seconds)


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def set_time(self, time):
        self.microwave.set_time(time)

    def add_time(self, time):
        self.microwave.add_time(time)

    def del_time(self, time):
        self.microwave.del_time(time)

    def show_time(self):
        return self.microwave.show_time()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
