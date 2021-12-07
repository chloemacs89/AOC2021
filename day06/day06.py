def solve1(data_lst, nb_days):
    for day in range(nb_days):
        current_nb = len(data_lst)
        for nb in data_lst:
            if not nb:
                data_lst.append(8)
        for k in range(current_nb):
            data_lst[k] -= 1 if data_lst[k] > 0 else -6

    return len(data_lst)


def solve2(data_lst, nb_days):
    future_add = data_lst[0]
    for day in range(nb_days):
        future_add = data_lst[0]
        for fsh in range(9):
            if fsh:
                data_lst[fsh-1] = data_lst[fsh]
        data_lst[6] += future_add
        data_lst[8] = future_add

    return sum(data_lst.values())


fish_type = {x: 0 for x in range(9)}
fish_type_test = {x: 0 for x in range(9)}

for d in [3, 4, 3, 1, 2]:
    if fish_type_test.get(d):
        fish_type_test[d] += 1
    else:
        fish_type_test[d] = 1

with open("/home/roflzyo/AOC/AOC_2021/day06/input.txt") as data_file:
    data = [int(x) for x in data_file.readline().strip("\n").split(",")]
    for d in data:
        if fish_type.get(d):
            fish_type[d] += 1
        else:
            fish_type[d] = 1

solve2(fish_type_test, 80)
solve2(fish_type, 256)
