file_path = "ingredients-input.txt"

class Range:
    def __init__(self, minimum, maximum):
        self.minimum = minimum  # Instance attribute
        self.maximum = maximum    # Instance attribute

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

    fresh = 0
    for id in ids:
        for range in ranges:
            if range.containsValue(id):
                fresh += 1
                break

print(fresh)