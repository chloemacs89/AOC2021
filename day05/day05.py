with open("/home/roflzyo/aoc/2021/day05/input.txt") as data_file:
    data = [line.strip("\n").split(" -> ") for line in data_file.readlines()]

cleared_data = [[(int(lst[0].split(",")[0]), int(lst[0].split(",")[1])), (int(lst[1].split(",")[0]), int(lst[1].split(",")[1]))] for lst in data]



def solve1(cleared_data):
    coordinates_count = {}
    for coor in cleared_data:
        x1 = coor[0][0]
        y1 = coor[0][1]
        x2 = coor[1][0]
        y2 = coor[1][1]
        if x1 == x2:
            for points in range(min(y1, y2), max(y1, y2)+1):
                coord = (x1, points)
                if coordinates_count.get(coord):
                    coordinates_count[coord] += 1
                else:
                    coordinates_count[coord] = 1
        elif y1 == y2:
            for points in range(min(x1, x2), max(x1, x2)+1):
                coord = (points, y1)
                if coordinates_count.get(coord):
                    coordinates_count[coord] += 1
                else:
                    coordinates_count[coord] = 1

    return len([1 for x in coordinates_count.values() if x >= 2])


solve1(cleared_data)

