test_data = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
             [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
             [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]

with open("/home/roflzyo/AOC/AOC_2021/day09/input.txt") as data_file:
    input_data = [[int(x) for x in row.strip("\n")] for row in data_file.readlines()]


def make_bassin(x, y, data, bassins):
    coords = ((-1, 0), (1, 0), (0, 1), (0, -1))
    try:
        val = data[x][y]
        if val == 9:
            return
        else:
            if bassins.get(data[x][y]):
                if (x, y) in bassins[data[x][y]]:
                    return
                else:
                    bassins[data[x][y]] += [(x, y)]
            else:
                bassins[data[x][y]] = [(x, y)]
    except IndexError:
        return
    for v, w in coords:
        if (x+v) >= 0 and (y+w) >= 0:
            make_bassin(x+v, y+w, data, bassins)


def count_bassins(bassins, bassins_count):
    bassins_len = sum([len(x) for x in bassins.values()])
    if bassins_count.get(bassins_len):
        bassins_count[bassins_len] += 1
    else:
        bassins_count[bassins_len] = 1


def solve1(data):
    min_points = []
    bassins_count = {}
    for x in range(len(data)):
        for y in range(len(data[0])):
            bassins = {}
            if data[x][y] == 9:
                pass
            elif x == 0 and y == 0:
                points = (
                    data[x][y],
                    data[x][y+1],
                    data[x+1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif x == 0 and y == len(data[0])-1:
                points = (
                    data[x][y],
                    data[x][y-1],
                    data[x+1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif x == len(data)-1 and y == 0:
                points = (
                    data[x][y],
                    data[x][y+1],
                    data[x-1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif x == len(data)-1 and y == len(data[0])-1:
                points = (
                    data[x][y],
                    data[x][y-1],
                    data[x-1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif y == 0:
                points = (
                    data[x][y],
                    data[x+1][y],
                    data[x][y+1],
                    data[x-1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif y == len(data[0])-1:
                points = (
                    data[x][y],
                    data[x+1][y],
                    data[x][y-1],
                    data[x-1][y]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif x == 0:
                points = (
                    data[x][y],
                    data[x+1][y],
                    data[x][y-1],
                    data[x][y+1]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            elif x == len(data)-1:
                points = (
                    data[x][y],
                    data[x-1][y],
                    data[x][y-1],
                    data[x][y+1]
                )
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)
            else:
                points = (data[x][y],
                          data[x-1][y],
                          data[x][y-1],
                          data[x][y+1],
                          data[x+1][y])
                if data[x][y] == min(points):
                    min_points += [data[x][y]+1]
                    bassins = {}
                    make_bassin(x, y, data, bassins)
                    count_bassins(bassins, bassins_count)

    sorted_bassins = sorted(bassins_count.keys())
    three_max_bassins = [sorted_bassins[-3], sorted_bassins[-2], sorted_bassins[-1]]
    print(three_max_bassins[0]*three_max_bassins[1]*three_max_bassins[2])
    return sum(min_points)


# print(solve1(test_data))
print(solve1(input_data))
