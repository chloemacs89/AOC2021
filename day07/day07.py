test_data = [16,1,2,0,4,2,7,1,2,14]

with open("/home/roflzyo/aoc/2021/day07/input.txt") as data_file:
    full_data = [int(x) for x in data_file.readline().strip("\n").split(",")]

def solve1(data_lst, non_linear=False):
    min_pos = min(data_lst)
    max_pos = max(data_lst)
    fuel_consumption = {}
    for pos in range(max(data_lst)):
        if non_linear:
            fuel_cons = sum([(abs(x-pos)*(abs(x-pos)+1)/2) for x in data_lst])
        else:
            fuel_cons = sum([abs(x-pos) for x in data_lst])
        fuel_consumption[pos] = fuel_cons
        
    return int(min(fuel_consumption.values()))

    
print(solve1(full_data))
print(solve1(full_data, non_linear=True))
