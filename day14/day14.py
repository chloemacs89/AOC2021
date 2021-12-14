s = "NNSOFOCNHBVVNOBSBHCB"

pairs = {}

with open("/home/roflzyo/AOC/AOC_2021/day14/input.txt") as f:
    for line in f.readlines():
        v, w = line.strip("\n").split(" -> ")
        pairs[v] = w


def init_pairs(template, lst=[]):
    if template[1:]:
        lst.append(template[0] + template[1])
        return init_pairs(template[1:], lst)
    else:
        return lst


def solve(template, pairs, n):
    lst = init_pairs(template)
    pairs_count = {}
    for letter in template:
        if pairs_count.get(letter):
            pairs_count[letter] += 1
        else:
            pairs_count[letter] = 1
    i = 0
    while i < n:
        new_lst = []
        for x in lst:
            if pairs_count.get(pairs[x]):
                pairs_count[pairs[x]] += 1
            else:
                pairs_count[pairs[x]] = 1
            new_lst.append(x[0] + pairs[x])
            new_lst.append(pairs[x] + x[1])
        lst = new_lst
        i += 1

    import pdb; pdb.set_trace()
    return pairs_count


j = solve(s, pairs, 10)
