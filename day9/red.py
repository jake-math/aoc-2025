file_path = "input.txt"

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y



with open(file_path, 'r') as file:
    coords = []
    for line in file:
        vals = line.strip().split(',')
        coords.append(Coordinate(int(vals[0]), int(vals[1])))

    maximum = -1
    for i in range(0, len(coords) - 1):
        for j in range(i + 1, len(coords)):
            coord1 = coords[i]
            coord2 = coords[j]

            x_dist = abs(coord1.x - coord2.x) + 1
            y_dist = abs(coord1.y - coord2.y) + 1

            area = x_dist * y_dist
            maximum = max(area, maximum)

print(maximum)