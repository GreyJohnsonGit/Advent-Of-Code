# read in data
def readInput(filename):
    rawData = open(filename, "r").read().split("\n")
    data = []
    for value in rawData:
        data.append(int(value))
    return data


# Part 1
def solution_part1(data):
    previous = {}    
    values = [-1, -1]

    for value in data:
        previous[2020 - value] = value
        if (previous.get(value) != None):
            values[0] = value
            values[1] = previous[value]

    result = values[0] * values[1]
    print("Numbers: " + str(values))
    return result

# Part 2
def solution_part2(data):
    previous = {}    
    values = [-1, -1, -1]

    for initialValue in data:
        for value in data:
            previous[2020 - initialValue - value] = value
            if (previous.get(value) != None):
                values[0] = value
                values[1] = previous[value]
                values[2] = initialValue
        previous.clear()

    result = values[0] * values[1] * values[2]
    print("Numbers: " + str(values))
    return result

data = readInput("inputs/Day1_input.txt")

print("2 Sum Result: " + str(solution_part1(data)))
print("3 Sum Result: " + str(solution_part2(data)))