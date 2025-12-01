file_path = "password-input.txt"
current = 50
zero_count = 0

def move_left(distance):
    global current
    current -= distance
    current %= 100

def move_right(distance):
    global current
    current += distance
    current %= 100

with open(file_path, 'r') as file:
    for line in file:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            move_left(distance)
        elif direction == 'R':
            move_right(distance)

        if current == 0:
            zero_count += 1

print(zero_count)