letter_dict = {}


def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


char_priority = 1
for char in range_char("a", "z"):
    letter_dict[char] = char_priority
    char_priority += 1

for char in range_char("A", "Z"):
    letter_dict[char] = char_priority
    char_priority += 1

pack_list = []

with open("rucksack_packing.txt", "r") as f:
    for line in f:
        pack_list.append(line.strip())

start_index = 0
grouped_list = []
for i in range(1, len(pack_list) + 1):
    if i % 3 == 0:
        grouped_list.append(pack_list[start_index:i])
        start_index = i

group_items_list = []
for group in grouped_list:
    first = group[0]
    second = group[1]
    third = group[2]
    for item in first:
        if item in second and item in third:
            group_items_list.append(item)
            break

total_priority = 0
for item in group_items_list:
    total_priority += letter_dict[item]

print(total_priority)
