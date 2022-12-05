sack_list = []
group_list = []
prio_list = []

#Open and read file to list
with open("day3.txt", "r") as f:
    for line in f:
        line = line.strip()
        sack_list.append([*line])


# Groups each rucksack into groups of 3.
for i in range(0, len(sack_list), 3):
    group_list.append( [sack_list[i], sack_list[i+1], sack_list[i+2]] )


for group in group_list:
    for value in group[0]:
        if (value in group[1]) and (value in group[2]):
            prio_list.append(value)
            break


print(prio_list)



    
    
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