import pandas as pd
raw_pack_list = []

stack1 = "TPZCSLQN"
stack2 = "LPTVHCG"
stack3 = "DCZF"
stack4 = "GWTDLMVC"
stack5 = "PWC"
stack6 = "PFJDCTSZ"
stack7 = "VWGBD"
stack8 = "NJSQHW"
stack9 = "RCQFSLV"

stack_list = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

original_layout = []
for stack in stack_list:
    original_layout.append([i for i in stack])

print(original_layout)

moving_list = []
with open("moving_plan.txt", "r") as f:
    for line in f:
        line_list = line.strip().split(" ")
        instruction_list = [int(line_list[1]), int(line_list[3]), int(line_list[5])]
        moving_list.append(instruction_list)

for move in moving_list:
    move_count = move[0]
    origin_loc = move[1]-1
    target_loc = move[2]-1
    for _ in range(move_count):
        box = original_layout[origin_loc].pop(-1)
        original_layout[target_loc].append(box)

for stack in original_layout:
    print(stack[-1])


