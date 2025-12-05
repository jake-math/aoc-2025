import functools

file_path = "ingredients-input.txt"

def compare(range1, range2):
    return range1.minimum - range2.minimum

class Range:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def containsValue(self, value):
        return value >= self.minimum and value <= self.maximum

with open(file_path, 'r') as file:
    ranges = []
    ids = []
    for line in file:
        id = line.strip().split('-')
        if len(id) == 2:
            ranges.append(Range(int(id[0]), int(id[1])))
        elif id[0] != '':
            ids.append(int(id[0]))

    ranges = sorted(ranges, key=functools.cmp_to_key(compare))

    left = 0
    right = 1
    while right < len(ranges):
        curr = ranges[left]
        next = ranges[right]

        if curr.maximum >= next.minimum:
            if curr.maximum > next.maximum:
                ranges.remove(next)
            else:
                ranges[left].maximum = next.maximum
                ranges.remove(next)
        else:
            left = right
            right = left + 1

    fresh = 0
    for range in ranges:
        fresh += range.maximum - range.minimum + 1

print(fresh)