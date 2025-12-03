file_path = "ids.txt"
sol = 0

def split_string_by_size(input_string, size):
    return [
        input_string[i : i + size]
        for i in range(0, len(input_string), size)
    ]

def findInvalidIds(min, max):
    global sol

    for curr in range(min, max + 1):
        currStr = str(curr)

        for split in range(len(currStr) - 1):
            if len(currStr) % (split + 1) == 0:
                if len(set(split_string_by_size(currStr, split + 1))) == 1:
                    sol += curr
                    break

with open(file_path, 'r') as file:
    ids = file.read().split(',')
    for id in ids:
        minMax = id.split('-')
        findInvalidIds(int(minMax[0]), int(minMax[1]))

print(sol)
