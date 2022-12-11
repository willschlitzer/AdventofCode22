from input import input_string


def unique_in_string(char4_string):
    if len(char4_string) != 4:
        return False
    char1 = char4_string[0]
    for char in char4_string[1:]:
        if char1 == char:
            return False
    char2 = char4_string[1]
    for char in char4_string[2:]:
        if char2 == char:
            return False
    if char4_string[2] == char4_string[3]:
        return False
    return True


for i, char in enumerate(input_string[:-3]):
    char4_string = input_string[i : i + 4]
    unique_status = unique_in_string(char4_string=char4_string)
    if unique_status:
        print(char4_string)
        print(i + 4)
        break
