import time
import calendar
from datetime import timedelta, datetime


def parse_time(string):
    """
    >>> parse_time("[1518-06-03 23:58] Guard #2399 begins shift")
    time.struct_time(tm_year=1518, tm_mon=6, tm_mday=3, tm_hour=23, tm_min=58, tm_sec=0, tm_wday=0, tm_yday=154, tm_isdst=-1)
    """
    time_string = string.split("]")[0][1:]
    return time.strptime(time_string, "%Y-%m-%d %H:%M")

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

def daterange(start_date, end_date):
    # """
    # >>> start_date = date(2013, 1, 1)
    # >>> end_date = date(2015, 6, 2)
    # >>> daterange(start_date, end_date)
    # """
    for n in range(int ((end_date - start_date).minutes)):
        yield start_date + timedelta(minutes=n)

    # start_date = datetime(2013, 1, 1)
    # end_date = datetime(2015, 6, 2)
    # for single_date in daterange(start_date, end_date):
    #     print(single_date)
    #     # print single_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    f = open('data/input-day4.txt')
    strings = sorted(list(f))
    for v, s in enumerate(strings):
        strings[v] = s.strip()

    guard2sleep = {}
    guard2min = {}

    current_guard = None
    awake = True

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

    best_guard = None
    time_asleep = -1
    for guard in guard2sleep.keys():
        mod = -1
        seconds = 0
        for t in guard2sleep[guard]:
            seconds = seconds + (mod * calendar.timegm(t))
            mod = mod * -1
        tg = int(seconds/60)
        if tg > time_asleep:
            time_asleep = tg
            best_guard = guard
    
    print(best_guard, time_asleep)
