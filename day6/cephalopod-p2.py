file_path = "input.txt"

def calculate(vals, index, operator):
    new_vals = []
    curr = ""
    numbers_found = True
    while numbers_found and index < len(vals[0]):
        numbers_found = False
        for i in range(0, len(vals)):
            if vals[i][index] != " ":
                numbers_found = True
                curr += vals[i][index]

        if numbers_found:
            new_vals.append(int(curr))

        curr = ""
        index += 1

    result = new_vals[0]
    for i in range(1, len(new_vals)):
        if operator == "+":
            result += new_vals[i]
        else:
            result *= new_vals[i]

    return result, index

with open(file_path, 'r') as file:
    sol = 0
    vals = []
    for line in file:
        curr = []
        for char in line.strip('\n'):
            curr.append(char)
        vals.append(curr)

    index = 0
    while index < len(vals[0]):
        operator = vals[len(vals) - 1][index]
        result = calculate(vals[0:len(vals) - 1], index, operator)
        sol += result[0]
        index = result[1]


print(sol)