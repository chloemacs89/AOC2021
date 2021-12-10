with open("/home/roflzyo/AOC/AOC_2021/day10/input.txt") as dt_file:
    data = [line.strip("\n") for line in dt_file.readlines()]


def make_score_list(symb_lst, score):
    completion_points = {")": 1, "]": 2, "}": 3, ">": 4}
    points = 0
    for symb in symb_lst:
        points *= 5
        points += completion_points[symb]

    score.append(points)


def solve1(data):
    points = 0
    symbols = {"(": ")", "[": "]", "{": "}", "<": ">"}
    point_tag = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = []
    for lst in data:
        added_symbols = []
        queue = []
        illegal = False
        for symb in lst:
            if symb in symbols.keys():
                queue.append(symb)
            else:
                if symb == symbols[queue[len(queue) - 1]]:
                    queue.pop()
                else:
                    points += point_tag[symb]
                    illegal = True
                    break

        if not illegal and queue:
            queue.reverse()
            for symb in queue:
                added_symbols.append(symbols[symb])

            make_score_list(added_symbols, score)

    score.sort()
    return (points, score[len(score)//2])


print(solve1(data))
