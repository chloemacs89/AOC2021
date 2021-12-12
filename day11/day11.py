with open("/home/roflzyo/aoc/2021/day11/input.txt") as data_file:
    data = [[int(x) for x in line.strip("\n")] for line in data_file.readlines()]


def flashes(x, y, data, has_flashed):
    coord = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    try:
        if data[x][y] == 9 and (x, y) not in has_flashed:
            data[x][y] = 0
            has_flashed.append((x, y))
            for v, w in coord:
                if x+v >= 0 and y+w >=0:
                    flashes(x+v, y+w, data, has_flashed)
        elif data[x][y] == 0 and (x, y) in has_flashed:
            pass
        else:
            data[x][y] += 1
    except IndexError:
        return
    


def solve(data):
    flashes_count = 0
    for n in range(100):
        has_flashed = []
        for x in range(len(data)):
            for y in range(len(data[0])):
                flashes(x, y, data, has_flashed)

        flashes_count += len(has_flashed)

    return flashes_count


def solve2(data):
    synchro_step = 0
    n = 0
    while True:
        n += 1
        has_flashed = []
        for x in range(len(data)):
            for y in range(len(data[0])):
                flashes(x, y, data, has_flashed)

        if data == [[0 for i in range(len(data[0]))] for j in range(len(data))]:
            synchro_step = n+100
            break
        
    return synchro_step


print(solve(data))
print(solve2(data))
