file_path = "ids.txt"
sol = 0

def findInvalidIds(min, max):
    global sol
    for curr in range(min, max):
        currStr = str(curr)

        half = len(currStr) // 2
        if currStr[0:half] == currStr[half:]:
            sol += curr



with open(file_path, 'r') as file:
    ids = file.read().split(',')
    for id in ids:
        minMax = id.split('-')
        findInvalidIds(int(minMax[0]), int(minMax[1]))

print(sol)
