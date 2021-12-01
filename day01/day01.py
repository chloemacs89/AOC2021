# First part

with open("./input.txt", "r") as data_file:
    data_list = [int(data) for data in data_file.readlines()]

print(sum([1 for x in range(len(data_list[1:])) if (data_list[x+1] > data_list[x])]))


# Second part

print(sum([1 for x in range(len(data_list[3:])) if (sum((data_list[x+3], data_list[x+2], data_list[x+1])) > sum((data_list[x+2], data_list[x+1], data_list[x])))]))
