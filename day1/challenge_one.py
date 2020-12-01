input = open("input.txt", "r")
list = []
for line in input:
    list.append(line)
for value in list:
    for value_two in list:
        if int(value) + int(value_two) == 2020:
            print(int(value) * int(value_two))
            exit()