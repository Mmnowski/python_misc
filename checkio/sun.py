def sun_angle(time):
    time_split = time.split(':')
    minute = 0.25
    int_time = int(time_split[0])*60+int(time_split[1])
    if int_time < 360 or int_time > 1080:
        return 'I don\'t see the sun!'
    return (int_time)*minute-90


print(sun_angle('18:00'))
