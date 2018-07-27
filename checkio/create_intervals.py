def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    intervals = []
    data = list(data)
    if len(data) == 0:
        return intervals
    elif len(data) == 1:
        intervals.append((data[0], data[0]))
        return intervals
    else:
        data.sort()
        print(data)
        start = data[0]
        end = 0
        for n in range(1, len(data)):
            if data[n-1]+1 == data[n]:
                end = data[n]
            else:
                if end < start:
                    end = start
                intervals.append((start, end))
                start = data[n]
                if n+1 == len(data):
                    if end != start:
                        end = start
                        intervals.append((start, end))
                # if data[n-1]+1 > data[n]:
                #     break
        if len(intervals) == 0 or start < end:
            intervals.append((start, end))
        return intervals


print(create_intervals({1}))
