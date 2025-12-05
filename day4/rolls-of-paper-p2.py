file_path = "paper.txt"
sol = 0

def is_paper(y, x, grid, y_max, x_max):
    if y < 0 or y > y_max or x < 0 or x > x_max:
        return False

    if grid[y][x] == '.':
        return False
    return True

def check_adjacent(y, x, grid, y_max, x_max):
    if grid[y][x] == '.':
        return 0

    adjacent_rolls = 0

    if y > 0:
        adjacent_rolls += is_paper(y - 1, x, grid, y_max, x_max)
        if x > 0:
            adjacent_rolls += is_paper(y - 1, x - 1, grid, y_max, x_max)
        if x < x_max:
            adjacent_rolls += is_paper(y - 1, x + 1, grid, y_max, x_max)
    if y < y_max:
        adjacent_rolls += is_paper(y + 1, x, grid, y_max, x_max)
        if x > 0:
            adjacent_rolls += is_paper(y + 1, x - 1, grid, y_max, x_max)
        if x < x_max:
            adjacent_rolls += is_paper(y + 1, x + 1, grid, y_max, x_max)
    if x > 0:
        adjacent_rolls += is_paper(y, x - 1, grid, y_max, x_max)
    if x < x_max:
        adjacent_rolls += is_paper(y, x + 1, grid, y_max, x_max)

    if adjacent_rolls <= 3:
        grid[y][x] = '.'

    return adjacent_rolls <= 3


with open(file_path, 'r') as file:
    grid = []

    y = 0
    for line in file:
        line = line.strip()
        grid.append([])
        for char in range(len(line)):
            grid[y].append(line[char])
        y += 1

    foundZero = False
    while not foundZero:
        removed = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                removed += check_adjacent(y, x, grid, len(grid) - 1, len(grid[y]) - 1)

        sol += removed
        if removed == 0:
            foundZero = True

print(sol)