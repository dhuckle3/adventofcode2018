import string

def checksum(data):
    lines = list(data)
    two_count = 0
    three_count = 0

    for line in lines:
        line = line.strip()
        has_two = False
        has_three = False

        for char in string.ascii_lowercase:
            count = line.count(char)
            if count is 2:
                has_two = True
            elif count is 3:
                has_three = True

            if has_two and has_three:
                break

        print(line, ", ", has_two, ", ", has_three)

        if has_two:
            two_count += 1
        if has_three:
            three_count += 1
    return two_count * three_count

def fuzzy_matcher(lines):
    """
    >>> fuzzy_matcher(['abc', 'ekg', 'abd'])
    'ab'
    """
    id = None
    for l1 in lines:
        for l2 in lines:
            l1 = l1.strip()
            l2 = l2.strip()
            if l1 is not l2:
                id = compare_lines(l1, l2)
                if id is not None:
                    return id
    return None

def compare_lines(l1, l2):
    """
    >>> compare_lines("abc", "abd")
    'ab'

    >>> compare_lines("aac", "abc")
    'ac'
    """
    mismatch_count = 0
    mismatch_index = -1
    
    for i, char in enumerate(l1):
        if len(l1) != len(l2):
            print(len(l1), len(l2))
            print(l1, l2)
        if i > len(l1) or i > len(l2):
            print(i, l1, l2)
        if char != l2[i]:
            mismatch_count += 1
            mismatch_index = i
    
    if mismatch_count is 1:
        return l1[0:mismatch_index] + l1[mismatch_index+1:len(l1)]
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()