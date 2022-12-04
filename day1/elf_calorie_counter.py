calorie_list = []

with open("elf_list.txt", "r") as f:
    for line in f:
        if line == "\n":
            calorie_list.append(None)
        else:
            calorie_list.append(int(line.strip()))


calorie_count = 0
total_calorie_list = []
for i in calorie_list:
    if not i:
        total_calorie_list.append(calorie_count)
        calorie_count = 0
    else:
        calorie_count += i

top_elf = max(total_calorie_list)
print(top_elf)

sorted_calorie_list = sorted(total_calorie_list, reverse=True)
top_three_elves = sum(sorted_calorie_list[0:3])
print(top_three_elves)
