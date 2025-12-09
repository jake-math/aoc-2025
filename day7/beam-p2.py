file_path = "input.txt"

def process_beams(map, beams, level, splits):
    while level < len(map):
        next_beams = set()
        for beam in beams:
            if map[level][beam] == '^':
                splits += 1
                if beam > 0:
                    next_beams.add(beam - 1)
                    splits += process_beams(map, next_beams, level + 1, splits)
                if beam < len(map):
                    next_beams.add(beam + 1)
                    splits += process_beams(map, next_beams, level + 1, splits)

with open(file_path, 'r') as file:
    splits = 0
    map = []
    beams = set()
    for line in file:
        curr = []
        for char in line.strip():
            curr.append(char)

        map.append(curr)

    for i in range(0, len(map[0])):
        if map[0][i] == 'S':
            beams.add(i)

    level = 1
    splits = 0
    process_beams(map, beams, level, splits)