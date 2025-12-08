file_path = "input.txt"

def calculate(vals, index, operator):
    result = vals[0][index]
    for i in range(1, len(vals) - 1):
        if operator == "+":
            result += vals[i][index]
        else:
            result *= vals[i][index]

    return result

def get_values(line):
    vals = []
    curr = ""
    for char in line:
        if char == " ":
            if curr != "":
                try:
                    vals.append(int(curr))
                    curr = ""
                except ValueError:
                    vals.append(curr)
                    curr = ""
        else:
            curr += char

    if curr != "":
        try:
            vals.append(int(curr))
        except ValueError:
            vals.append(curr)

    return vals

with open(file_path, 'r') as file:
    sol = 0
    count = 0
    vals = []
    for line in file:
        vals.append(get_values(line.strip()))

    for index in range(0, len(vals[0])):
        operator = vals[4][index]
        sol += calculate(vals, index, operator)

print(sol)