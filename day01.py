def read_frequencies(changes, frequency):
    """
    >>> read_frequencies(changes, frequency)
    """
    first_seen_twice = None
    for change in changes:
        frequency += int(change)
        if first_seen_twice is None and frequency in past_frequencies:
            first_seen_twice = frequency
        past_frequencies.add(frequency)

    return [frequency, first_seen_twice]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('data/input-day1.txt', 'r')
    lines = list(file)
    past_frequencies = set()
    result = read_frequencies(lines, 0)

    print('final frequency after first run', result[0])

    while(result[1] is None):
        result = read_frequencies(lines, result[0])
    print('First encountered twice:', result[1])
    # final frequency after first run 525
    # First encountered twice: 75749