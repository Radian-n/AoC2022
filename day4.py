group_list = []

with open("day4.txt", "r") as f:
    for line in f:
        pair = line.strip().split(",")

        cleaing_group = []
        for value in pair:
            value_split = value.split("-")
            lower = int(value_split[0])
            upper = int(value_split[1])
            pair = lower, upper
            cleaing_group.append(pair)
        group_list.append(cleaing_group)



subset_pair_count = 0

for group in group_list:
    g1 = group[0]
    g2 = group[1]
    # print(g1, g2)

    # Checking if group2 is subset of group1:
    if ( g2[0] >= g1[0] ) and ( g2[1] <= g1[1] ):
        # group2 is subset of group 1
        subset_pair_count += 1

    elif ( g1[0] >= g2[0] ) and ( g1[1] <= g2[1 ]):
        subset_pair_count += 1
    # Cheking if group1 is subset of group2:

print(subset_pair_count)