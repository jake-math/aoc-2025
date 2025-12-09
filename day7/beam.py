file_path = "input.txt"

with open(file_path, 'r') as file:
    count = 0
    beams = set()
    splits = 0
    for line in file:
        cleaned_line = line.strip()
        next_beams = set()
        if count == 0:
            for i in range(0, len(cleaned_line)):
                if cleaned_line[i] == 'S':
                    next_beams.add(i)

            count += 1
        else:
            for beam in beams:
                if cleaned_line[beam] == '^':
                    splits += 1
                    if beam > 0:
                        next_beams.add(beam - 1)
                    if beam < len(cleaned_line) - 1:
                        next_beams.add(beam + 1)
                else:
                    next_beams.add(beam)

        beams = next_beams

    print(beams)
    print(splits)