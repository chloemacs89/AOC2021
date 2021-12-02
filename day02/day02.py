# part 1

horizontal = 0
depth = 0

with open("./input.txt", "r") as data_file:
    for line in data_file.readlines():
        if line.split()[0] == "forward":
            horizontal += int(line.split()[1])
        elif line.split()[0] == "up":
            depth -= int(line.split()[1])
        else:
            depth += int(line.split()[1])

print(horizontal*depth)


# part 2

horizontal = 0
depth = 0
aim = 0

with open("./input.txt", "r") as data_file:
    for line in data_file.readlines():
        if line.split()[0] == "forward":
            horizon_aim = int(line.split()[1])
            horizontal += horizon_aim
            depth += horizon_aim*aim
        elif line.split()[0] == "up":
            aim += -int(line.split()[1])
        else:
            aim += int(line.split()[1])

print(horizontal*depth)
