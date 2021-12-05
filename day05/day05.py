test_data = [[(0, 9), (5, 9)], [(8, 0), (0, 8)], [(9, 4), (3, 4)],
             [(2, 2), (2, 1)], [(7, 0), (7, 4)], [(6, 4), (2, 0)],
             [(0, 9), (2, 9)], [(3, 4), (1, 4)], [(0, 0), (8, 8)],
             [(5, 5), (8, 2)]]

with open("/home/roflzyo/aoc/2021/day05/input.txt") as data_file:
    data = [line.strip("\n").split(" -> ") for line in data_file.readlines()]

cleared_data = [[(int(lst[0].split(",")[0]), int(lst[0].split(",")[1])),
                 (int(lst[1].split(",")[0]), int(lst[1].split(",")[1]))]
                for lst in data]


def solve(cleared_data, diagonals=False):
    coordinates_count = {}
    for coor in cleared_data:
        x1 = coor[0][0]
        y1 = coor[0][1]
        x2 = coor[1][0]
        y2 = coor[1][1]
        if diagonals:
            if (x1 == y2 and x2 == y1) or ((x1+y1)==(x2+y2)): 
                x = x1
                y = y1
                while True:
                    coord = (x, y)
                    if coordinates_count.get(coord):
                        coordinates_count[coord] += 1
                    else:
                        coordinates_count[coord] = 1
                    if x1 > x2:
                        x -= 1
                        y += 1
                    else:
                        x += 1
                        y -= 1
                    if coord == (x2, y2):
                        break
            elif (x1 == x2 and y1 == y2) or ((x1-y1)==(x2-y2) or (y1-x1)==(y2-x2)):
                x = x1
                y = y1
                while True:
                    coord = (x, y)
                    if coordinates_count.get(coord):
                        coordinates_count[coord] += 1
                    else:
                        coordinates_count[coord] = 1
                    if x1 > x2:
                        x -= 1
                        y -= 1
                    else:
                        x += 1
                        y += 1
                    if coord == (x2, y2):
                        break
        if x1 == x2:
            for points in range(min(y1, y2), max(y1, y2) + 1):
                coord = (x1, points)
                if coordinates_count.get(coord):
                    coordinates_count[coord] += 1
                else:
                    coordinates_count[coord] = 1
        elif y1 == y2:
            for points in range(min(x1, x2), max(x1, x2) + 1):
                coord = (points, y1)
                if coordinates_count.get(coord):
                    coordinates_count[coord] += 1
                else:
                    coordinates_count[coord] = 1

    return len([1 for x in coordinates_count.values() if x >= 2])


solve_1 = solve(cleared_data)
solve_2 = solve(cleared_data, diagonals=True)
print("part 1 :", solve_1)
print("part 2 :", solve_2)
