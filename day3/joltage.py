file_path = "batteries.txt"
sol = 0

with open(file_path, 'r') as file:
    for line in file:
        maximum = 0
        for i in range(0, len(line) - 1):
            for j in range(i + 1, len(line)):
                maximum = max(maximum, int("" + line[i] + line[j]))

        sol += maximum

print(sol)