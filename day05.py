from string import ascii_lowercase

def remove_duplicate(string):
    """
    >>> remove_duplicate("aaBBaAaA")
    'aaBBaA'
    >>> remove_duplicate("aA")
    ''
    >>> remove_duplicate("aaaA")
    'aa'
    """
    i = 0
    while i < len(string) -1 :
        first = string[i]
        second = string[i+1]
        if first != second and first.upper() == second.upper():
            first_part = string[0:i]
            second_part = string[i+2:len(string)]
            return first_part + second_part
        i = i + 1
    return string

def fully_react(string):
    """
    >>> fully_react("aaBBaAaA")
    'aaBB'
    """
    length = len(string)
    while True:
        string = remove_duplicate(string)
        if len(string) == length:
            break
        length = len(string)
    return string


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    fi = open('data/input-day05.txt', 'r')
    data = fi.read().replace('\n', '')

    # part 1
    new_polymer = fully_react(data)
    print(len(new_polymer))        

    # part 2
    smallest_polymer = new_polymer
    for c in ascii_lowercase:
        temp_polymer = new_polymer.replace(c, "")
        temp_polymer = temp_polymer.replace(c.upper(), "")
        temp_polymer = fully_react(temp_polymer)
        if len(temp_polymer) < len(smallest_polymer):
            smallest_polymer = temp_polymer
    print(len(smallest_polymer))



