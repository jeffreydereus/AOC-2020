class challenge_one:
    input = open("input.txt", "r")
    list = []
    for line in input:
        list.append(line)
    loop_number = -1
    found = False
    while not found:
        loop_number += 1
        for value in list:
            if int(list[loop_number]) + int(value) == 2020:
                found = True
                print(int(list[loop_number]) * int(value))