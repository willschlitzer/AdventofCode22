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
        pack_list.append(line)

misspacked_list = []
for pack in pack_list:
    n = len(pack)
    first_compartment = pack[: n // 2]
    second_compartment = pack[n // 2 :]
    for item in first_compartment:
        if item in second_compartment:
            misspacked_list.append(item)
            break

total_priority = 0
for item in misspacked_list:
    total_priority += letter_dict[item]

print(total_priority)
