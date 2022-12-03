
# Initialise calorie list
total_cal_list = []


with open("day1.txt", "r") as f:
    cal_count = 0

    for line in f:
        if line == "\n":
            total_cal_list.append(cal_count)
            cal_count = 0
        else:
            data = int(line.strip())
            cal_count += data
    total_cal_list.append(cal_count)


total_cal_list.sort(reverse=True)
total = 0

for i in range(0, 3):
    total += total_cal_list[i]

print(total)

