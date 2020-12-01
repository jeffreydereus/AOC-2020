input = open("input.txt", "r")
list = []
for line in input:
    list.append(line)
for value in list:
    for value_two in list:
        for value_three in list:
            numbers = [int(value), int(value_two), int(value_three)]
            if sum(numbers) == 2020:
                print(int(value) * int(value_two) * int(value_three))
                exit()