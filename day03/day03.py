# PART 1

gamma_rate = []
epsilon_rate = []

with open("/home/roflzyo/AOC/AOC_2021/day03/input.txt", "r") as data_file:
    matrice = [[x for x in y if x != "\n"] for y in data_file.readlines()]

for mat in range(len(matrice[0])):
    transpose_matrice = [x[mat] for x in matrice]
    ones = transpose_matrice.count("1")
    zeros = transpose_matrice.count("0")
    if ones > zeros:
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")

gamma = int("".join(gamma_rate), 2)
epsilon = int("".join(epsilon_rate), 2)
print(gamma * epsilon)

# PART 2


def find_rating(data_list, bit_criteria):
    rating_list = data_list[:]
    while len(rating_list) != 1:
        for mat in range(len(rating_list[0])):
            if len(rating_list) > 1:
                transpose = [x[mat] for x in rating_list]
                ones = transpose.count("1")
                zeros = transpose.count("0")
                temp_list = rating_list[:]
                if bit_criteria == "1":
                    for i in temp_list:
                        if ones >= zeros and i[mat] != "1":
                            rating_list.remove(i)
                        elif zeros > ones and i[mat] != "0":
                            rating_list.remove(i)
                elif bit_criteria == "0":
                    for i in temp_list:
                        if ones < zeros and i[mat] != "1":
                            rating_list.remove(i)
                        elif zeros <= ones and i[mat] != "0":
                            rating_list.remove(i)

    return rating_list[0]


oxygen_rating = int("".join(find_rating(matrice, "1")), 2)
co2_rating = int("".join(find_rating(matrice, "0")), 2)

print(oxygen_rating * co2_rating)
