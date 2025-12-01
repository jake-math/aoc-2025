file_path = "password-input.txt"
current = 50
zero_count = 0

def count_zeros(start, move):
    direction = 1 if move > 0 else -1
    steps = abs(move)

    hits = 0
    for i in range(1, steps + 1):
        if (start + i * direction) % 100 == 0:
            hits += 1

    return hits


with open(file_path) as file:
    for line in file:
        direction = line[0]
        distance = int(line[1:])

        delta = distance if direction == "R" else -distance

        zero_count += count_zeros(current, delta)
        current = (current + delta) % 100

print(zero_count)
