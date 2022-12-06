state_data_input = []
instruction_input = []
stack_list = []
state_input = True
stack_size = 0

with open("day5.txt", "r") as f:
    for line in f:
        # Checks if finished reading state data.
        if line[0:2] == " 1":
            state_input = False

        # determines crate location based on line length.
        if state_input == True:
            columns = len(line) // 4
            for i in range(0, len(line)-3, 4):
                data = line[i:i+4]
                data = data.strip().replace("[", "").replace("]", "")
                col = i // 4 + 1
                data_tup = data, col
                state_data_input.append(data_tup)

                # Records how many stacks there are
                if col > stack_size:
                    stack_size = col

        if state_input == False:
            line = line.strip()
            if "move " in line:
                # Finds the quantity that will be moved from the input line string
                quant_end_i = line.find(" from")
                move_quant = line[5:quant_end_i]

                # Finds the origin from input line string
                origin_start_i = line.find("from ") + 5
                origin_end_i = line.find(" to")
                move_origin = line[origin_start_i:origin_end_i]


                # Finds the destination from input line string
                dest_start_i = origin_end_i + 4
                move_dest = line[dest_start_i:]

                instruction_input.append((move_quant, move_origin, move_dest))



# Creating Stacks - Master is a list, and then each index corresponds to a stack list
for i in range(0, stack_size+1):
    if i == 0:
        stack_list.append(None)
    else:
        new_list = []
        stack_list.append(new_list)
print(stack_list)



# Initialising Stack and Crate Setup
state_data_input.reverse() # Reverse data so crates are added from the bottom
for data in state_data_input:
    if data[0] != "":
        stack = data[1]
        crate = data[0]
     
        stack_list[stack].append(crate)

print(stack_list)

# Go through instruction set and move crates
for inst in instruction_input:
    quantity = int(inst[0])
    origin = int(inst[1])
    destination = int(inst[2])

    # Repeats move instructions based on quantity integer
    for moves in range(0, quantity):
        removed_crate = stack_list[origin].pop()
        stack_list[destination].append(removed_crate)


# Get crates on top of stacks:
output_str = ""

for i in range(1, len(stack_list)):
    output_str += stack_list[i][-1]

print(output_str)