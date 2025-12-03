file_path = "batteries.txt"
sol = 0

def findLargest(line):
    currBatteries = ""
    leftPointer = 0

    for batteryNumber in range(1, 13):
        currMax = -1
        for i in range(leftPointer, len(line) - (12 - batteryNumber)):
            currMax = max(currMax, int(line[i]))

        currBatteries = currBatteries + str(currMax)
        for i in range(leftPointer, len(line) - (12 - batteryNumber)):
            if line[i] == str(currMax):
                leftPointer = i + 1
                break

    global sol
    sol += int(currBatteries)

with open(file_path, 'r') as file:
    for line in file:
        findLargest(line.strip())

print(sol)