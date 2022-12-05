sack_list = []
prio_list = []

with open("day3.txt", "r") as f:
    for line in f:
        line = line.strip()
        mid_index = len(line) // 2
        comp1 = line[0:mid_index]
        comp2 = line[mid_index:]
        # print(line + "  -  " + str(mid_index))
        # print(comp1 + " " + comp2)
        rucksack = [*comp1], [*comp2]
        sack_list.append(rucksack)
    
    

for sack in sack_list:
    for value in sack[0]:
        if value in sack[1]:
            prio_list.append(value)
            break

total = 0
for prio_letter in prio_list:
    if prio_letter.islower():
        prio_int = ord(prio_letter) - 96
        # print("LOWER  " + prio_letter + str(prio_int))

    elif prio_letter.isupper():
        prio_int = ord(prio_letter) - 38
        # print("UPPER  " + prio_letter + str(prio_int))
    else:
        prio_int = 0
    total += prio_int

print(total)