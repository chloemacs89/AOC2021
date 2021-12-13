with open("/home/roflzyo/AOC/AOC_2021/day13/input.txt") as f:
    coord = []
    for line in f.readlines():
        v, w = line.strip("\n").split(",")
        coord.append((int(v), int(w)))

with open("/home/roflzyo/AOC/AOC_2021/day13/fold.txt") as f_d:
    fold = []
    for line in f_d.readlines():
        c, d = line.strip("\n").split()[2].split("=")
        fold.append((c, int(d)))

max_x = max([x[0] for x in coord])+1
max_y = max([x[1] for x in coord])+1


def make_chart(coordinates, max_x, max_y):
    chart = []
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append("#") if (x, y) in coordinates else row.append(".")
        chart.append(row)

    return chart


def fold_chart(chart, folding):
    for fold in folding:
        if fold[0] == "x":
            for y in range(len(chart)):
                for x in range(len(chart[0])):
                    if x != fold[1]:
                        new_x = fold[1]*2-x
                        if chart[y][x] == ".":
                            chart[y][x] = chart[y][new_x]
                chart[y] = chart[y][:fold[1]]
        else:
            for y in range(len(chart)):
                for x in range(len(chart[0])):
                    if y != fold[1]:
                        new_y = fold[1]*2 - y
                        if chart[y][x] == ".":
                            chart[y][x] = chart[new_y][x]
            chart.pop(fold[1])
            chart = chart[:fold[1]]

    return chart


def count_hashes(chart):
    return len([1 for y in chart for x in y if x == "#"])


chart = make_chart(coord, max_x, max_y)
new_chart = fold_chart(chart, [("x", 655)])
count_hashes(new_chart)

full_chart = fold_chart(chart, fold)
for x in full_chart:
    print("".join(x))
