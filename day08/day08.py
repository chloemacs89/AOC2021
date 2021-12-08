with open("/home/roflzyo/AOC/AOC_2021/day08/input.txt") as data_file:
    input_data = []
    output_data = []
    for line in data_file.readlines():
        data = line.strip("\n").split(" | ")
        input_data.append(data[0].split(" "))
        output_data.append(data[1].split(" "))

print(len([1 for sub in output_data for elem in sub if len(elem) in (2, 3, 4, 7)]))

def get_from_one(one_str, flat_str, digit_graph):
    for letter in one_str:
        if flat_str.count(letter) == 9:
            digit_graph[6] = letter
        else:
            digit_graph[3] = letter


def get_from_seven(letter, digit_graph):
    digit_graph[1] = letter


def get_from_four(four_str, flat_str, digit_graph):
    for letter in four_str:
        if flat_str.count(letter) == 7:
            digit_graph[4] = letter
        else:
            digit_graph[2] = letter

def get_digit(digit_graph):
    return {
        "".join(sorted(digit_graph[1]+digit_graph[2]+digit_graph[3]+digit_graph[5]+digit_graph[6]+digit_graph[7])):0,
        "".join(sorted(digit_graph[3]+digit_graph[6])):1,
        "".join(sorted(digit_graph[1]+digit_graph[3]+digit_graph[4]+digit_graph[5]+digit_graph[7])):2,
        "".join(sorted(digit_graph[1]+digit_graph[3]+digit_graph[4]+digit_graph[6]+digit_graph[7])):3,
        "".join(sorted(digit_graph[2]+digit_graph[3]+digit_graph[4]+digit_graph[6])):4,
        "".join(sorted(digit_graph[1]+digit_graph[2]+digit_graph[4]+digit_graph[6]+digit_graph[7])):5,
        "".join(sorted(digit_graph[1]+digit_graph[2]+digit_graph[4]+digit_graph[5]+digit_graph[6]+digit_graph[7])):6,
        "".join(sorted(digit_graph[1]+digit_graph[3]+digit_graph[6])):7,
        "abcdefg":8,
        "".join(sorted(digit_graph[1]+digit_graph[2]+digit_graph[3]+digit_graph[4]+digit_graph[6]+digit_graph[7])):9
    }


def solve2(in_data, out_data):
    output_value = []
    for seg in range(len(in_data)):
        current_seg = sorted(in_data[seg], key=len)
        flat_str = "".join(sorted("".join(current_seg)))
        digit_graph = {}
        for dig in current_seg[:3]:
            if len(dig) == 2:
                one = dig
                get_from_one(dig, flat_str, digit_graph)
                for ltr in dig:
                    flat_str = flat_str.replace(ltr, "")
            elif len(dig) == 3:
                letter = dig
                for ltr in one:
                    letter = letter.replace(ltr, "")
                get_from_seven(letter, digit_graph)
                flat_str = flat_str.replace(letter, "")
            elif len(dig) == 4:
                letters = dig
                for ltr in one:
                    letters = letters.replace(ltr, "")
                get_from_four(letters, flat_str, digit_graph)
                for ltr in letters:
                    flat_str = flat_str.replace(ltr, "")
        rem1 = flat_str[0]
        rem2 = flat_str[-1]
        digit_graph[5] = rem1 if flat_str.count(rem1) == 4 else rem2
        digit_graph[7] = rem1 if flat_str.count(rem1) == 7 else rem2

        current_graph = get_digit(digit_graph)

        values = [str(current_graph["".join(sorted(x))]) for x in out_data[seg]]
        output_value.append(int("".join(values)))

    return sum(output_value)


print(solve2(input_data, output_data))
