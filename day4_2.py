group_list = []
master_list = []

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


overlap_count = 0

for group in group_list:
    g1 = group[0]
    g2 = group[1]

    g1_range = [x for x in range(g1[0], g1[1]+1)]
    g2_range = [y for y in range(g2[0], g2[1]+1)]

    total_length = len(g1_range) + len(g2_range)
    exclusive_length = len(list(set(g1_range + g2_range)))

    if total_length != exclusive_length:
        overlap_count += 1
    
print(overlap_count)
