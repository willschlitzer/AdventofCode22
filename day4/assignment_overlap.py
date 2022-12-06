elf_assignments = []

def split_elf(input_range_string):
    assignment_range = input_range_string.split("-")
    return [int(assignment_range[0]), int(assignment_range[1])]

with open("assignments.txt", "r") as f:
    for line in f:
        split_line = line.strip().split(",")
        first_elf = split_line[0]
        second_elf = split_line[1]
        elf_assignments.append([split_elf(first_elf), split_elf(second_elf)])

overlap_contain_counter = 0

for assignment_pair in elf_assignments:
    elf1 = assignment_pair[0]
    elf2 = assignment_pair[1]
    if (elf1[0] >= elf2[0]) and (elf1[1]<=elf2[1]):
        overlap_contain_counter += 1
    elif (elf2[0] >= elf1[0]) and (elf2[1]<=elf1[1]):
        overlap_contain_counter += 1

print(overlap_contain_counter)

pair_overlap_container = 0

for assignment_pair in elf_assignments:
    elf1 = assignment_pair[0]
    elf2 = assignment_pair[1]
    elf1_range = range(elf1[0], elf1[1]+1)
    elf2_range = range(elf2[0], elf2[1]+1)
    overlap = False
    for i in elf1_range:
        if i in elf2_range:
            pair_overlap_container += 1
            overlap = True
            break
        if overlap:
            break

print(pair_overlap_container)
