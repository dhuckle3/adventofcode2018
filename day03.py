def make_container(w, h):
    """
    >>> make_container(3,2)
    [[[], [], []], [[], [], []]]
    """
    return [[[] for x in range(w)] for y in range(h)] 

def add_rect_string(rect, some_string):
    """
    >>> rect = make_container(3,3)
    >>> add_rect_string(rect, '#1 @ 2,2: 1x1')
    >>> count_claims(rect, 1)
    1
    >>> add_rect_string(rect, '#2 @ 1,2: 1x1')
    >>> count_claims(rect, 1)
    2
    """
    rect_args = some_string.split(" ")
    id = rect_args[0]
    [x,y] = rect_args[2][:-1].split(",")
    [width, height] = rect_args[3].split("x")
    return add_rect(rect, id, int(x), int(y), int(width), int(height))

def add_rect(rect, id, x, y, width, height):
    """
    >>> rect = [[[], [], []], [[], [], []]]
    >>> add_rect(rect, '#1', 1, 1, 2, 1)
    >>> rect
    [[[], [], []], [[], [\'#1\'], [\'#1\']]]
    """
    for j in range(x, x+width):
        for i in range(y, y+height):
            rect[i][j].append(id)

def count_claims(container, minimum_claims):
    """
    >>> rect = make_container(3,3)
    >>> add_rect(rect, '1', 2, 2, 1, 1)
    >>> count_claims(rect, 1)
    1
    >>> add_rect(rect, '2', 1, 2, 1, 1)
    >>> count_claims(rect, 1)
    2
    """
    count = 0
    for y in container:
        for x in y:
            if len(x) >= minimum_claims:
                count += 1
    return count

def non_overlapping_positions(contianer):
    claims = set()
    multi_claims = set()
    for row in contianer:
        for column in row:
            if len(column) == 1:
                claims.add(column[0])
            else:
                for claim in column:
                    multi_claims.add(claim)

    return claims.difference(multi_claims)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Solution
    container = make_container(1000,1000)
    f = open('data/input-day3.txt')
    lines = list(f)
    for line in lines:
        add_rect_string(container, line.strip())
    print('part1: spaces with 2 or more IDs', count_claims(container, 2))

    non_overlapping = non_overlapping_positions(container)
    for id in non_overlapping:
        print("part2: Found non overlapping id", id)
