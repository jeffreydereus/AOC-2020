import re
input = open("input.txt", "r")
list = []
correct_passwords = []
for line in input:
    list.append(line)
for value in list:
    match = re.match(r'([0-9]{1,2})\-([0-9]{1,2})\s([a-z]{1})\:\s([a-z]*)', value, re.I | re.U)
    if match is not None:
        if match.group(4).count(match.group(3)) >= int(match.group(1)) and match.group(4).count(match.group(3)) <= int(match.group(2)):
            correct_passwords.append(match)
print(len(correct_passwords))