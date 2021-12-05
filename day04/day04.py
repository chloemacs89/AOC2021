import re
from copy import deepcopy

first_line = 0
grid = []
subgrid = []

with open("/home/roflzyo/aoc/2021/day04/input.txt") as data_file:
    for line in data_file.readlines():
        if not first_line:
            numbers = [int(x) for x in line.strip("\n").split(",")]
            first_line = 1
        elif line != "\n":
            row = line.lstrip(" ").strip("\n")
            row = re.sub(r"\s+", ",", row)
            r = [int(x) for x in row.split(",")]
            subgrid.append(r)
        elif line == "\n" and len(subgrid) == 5:
            grid.append(subgrid)
            subgrid = []
    grid.append(subgrid)
    del subgrid

inverted_grid = []

for mat in grid:
    subgrid = []
    for x in range(len(mat[0])):
        row = [y[x] for y in mat]
        subgrid.append(row)
    inverted_grid.append(subgrid)
    

def bingo_dispenser(numbers_list, n):
    return set(numbers_list[0:n])
    

def bingo(numbers_list, row_list, col_list):
    winner = False
    nb = 5
    nb_list = bingo_dispenser(numbers_list, nb)
    while not winner:
        for i in range(len(row_list)):
            for j in range(len(row_list[i])):
                if len(nb_list.intersection(row_list[i][j])) == 5:
                    winner = True
                    grid_winner_index = i
                    last_number = numbers_list[nb-1]
                    break
                elif len(nb_list.intersection(col_list[i][j])) == 5:
                    winner = True
                    grid_winner_index = i
                    last_number = numbers_list[nb-1]
                    break
        second_round = True
        if second_round and nb >= 11:
            nb += 1
            nb_list = bingo_dispenser(numbers_list, nb)
        elif second_round:
            nb += 6
            nb_list = bingo_dispenser(numbers_list, nb)

    return (row_list[grid_winner_index], nb_list, last_number, col_list[grid_winner_index])

def bingo_squid_win(numbers_list, row_list, col_list):
    skip_list = []
    nb = 5
    nb_list = bingo_dispenser(numbers_list, nb)
    while len(skip_list) != 200:
        for i in range(len(row_list)):
            if row_list[i] not in skip_list:
                for j in range(len(row_list[i])):
                    if len(nb_list.intersection(set(row_list[i][j]))) == 5 or len(nb_list.intersection(set(col_list[i][j]))) == 5:
                        print(row_list[i])
                        print(col_list[i])
                        grid_winner_index = i
                        last_number = numbers_list[nb-1]
                        skip_list.append(row_list[i])
                        skip_list.append(col_list[i])
                        break
        second_round = True
        if second_round and nb >= 11:
            nb += 1
            nb_list = bingo_dispenser(numbers_list, nb)
        elif second_round:
            nb += 6
            nb_list = bingo_dispenser(numbers_list, nb)

    return (skip_list[len(skip_list)-1], nb_list, last_number)


def find_solution(numbers_list, row_list, col_list, squid_win=False):
    if squid_win:
        value = bingo_squid_win(numbers_list, row_list, col_list)
    else:
        value = bingo(numbers_list, row_list, col_list)
    grid_numbers = [nb for lst in value[0] for nb in lst]
    unfind_numbers = set(grid_numbers).difference(value[1])
    print(value[2])
    return sum(unfind_numbers) * value[2]

print(find_solution(numbers, grid, inverted_grid))
print(find_solution(numbers, grid, inverted_grid, squid_win=True))


