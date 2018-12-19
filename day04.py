import calendar
from datetime import timedelta, datetime

def parse_time(string):
    """
    >>> parse_time("[1518-06-03 23:58] Guard #2399 begins shift")
    datetime.datetime(1518, 6, 3, 23, 58)
    """
    time_string = string.split("]")[0][1:]
    return datetime.strptime(time_string, "%Y-%m-%d %H:%M")

def parse_message(string):
    """
    >>> m1 = "[1518-06-03 23:58] Guard #2399 begins shift"
    >>> m2 = "[1518-10-06 00:05] falls asleep"
    >>> m3 = "[1518-08-17 00:55] wakes up"
    >>> m4 = "[1518-06-03 23:58] Guard #1 begins shift"
    >>> parse_message(m1)
    ['start', '#2399']
    >>> parse_message(m2)
    ['sleep']
    >>> parse_message(m3)
    ['wake']
    >>> parse_message(m4)
    ['start', '#1']
    """
    message = string.split("]")[1].strip()
    if message[0] is 'G':
        guard = message.split(' ')[1]
        return ['start', guard]
    elif "falls asleep" in message:
        return ['sleep']
    elif "wakes up" in message:
        return ['wake']
    else:
        return None

def dt_range(start_date, end_date):
    """
    >>> start_time = parse_time("[1518-06-03 23:58] Guard #2399 begins shift")
    >>> end_time = parse_time("[1518-06-04 00:02] ends shift")
    >>> for i in dt_range(start_time, end_time):
    ...     print(i)
    1518-06-03 23:58:00
    1518-06-03 23:59:00
    1518-06-04 00:00:00
    1518-06-04 00:01:00
    """
    instant = start_date
    while instant < end_date:
        yield instant
        instant = instant + timedelta(minutes=1)

def create_guard_dict(messages):
    guard2sleep = {}
    current_guard = None

    for msg in sorted(strings):
        t = parse_time(msg)
        m = parse_message(msg)

        if m[0] is 'start':
            current_guard = m[1]
            if current_guard not in guard2sleep:
                guard2sleep[current_guard] = []
        elif m[0] is 'sleep':
                guard2sleep[current_guard].append(t)
        elif m[0] is 'wake':
                guard2sleep[current_guard].append(t)
    return guard2sleep

def most_minutes_slept(guard2sleep):
    best_guard = None
    time_asleep = -1
    for guard in guard2sleep.keys():
        mod = -1
        seconds = 0
        for t in guard2sleep[guard]:
            seconds = seconds + (mod * t.timestamp())
            mod = mod * -1
        tg = int(seconds/60)

        if tg > time_asleep:
            time_asleep = tg
            best_guard = guard

    return [best_guard, time_asleep]

def minute_most_often_asleep(times):
    minute_array = [0] * 60

    i = 0
    while i+1 < len(times):
        start_t = times[i]
        end_t = times[i+1]
        i = i + 2
        for instant in dt_range(start_t, end_t):
            minute = instant.minute
            minute_array[minute-1] = minute_array[minute-1] + 1
            
    most_minutes_slept = -1
    minute = -1

    for i in range(60):
        if minute_array[i] > most_minutes_slept:
            most_minutes_slept = minute_array[i]
            minute = i +1
    return [most_minutes_slept, minute]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    f = open('data/input-day4.txt')
    strings = sorted(list(f))
    for v, s in enumerate(strings):
        strings[v] = s.strip()

    guard2sleep = create_guard_dict(strings)
    guard2min = {}

    # Find minutes slept for each guard
    [best_guard, time_asleep] = most_minutes_slept(guard2sleep)
    print(best_guard, time_asleep)

    # find the minute most slept by the guard
    [most_minutes_slept, minute] = minute_most_often_asleep(guard2sleep[best_guard])
    print(most_minutes_slept, minute)
    
    # part 1
    print(minute*int(best_guard[1:]))

    # find minutes most sleept by any guard on a specific minute
    best_guard = None
    most_times = -1
    minute_asleep = -1
    for guard in guard2sleep.keys():
        times = guard2sleep[guard]
        [times_asleep, minute] = minute_most_often_asleep(times)
        if times_asleep > most_times:
            most_times = times_asleep
            minute_asleep = minute
            best_guard = guard
    print('guard, most_minutes, minute')
    print(minute_asleep*int(best_guard[1:]))
