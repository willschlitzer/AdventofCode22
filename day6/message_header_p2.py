from input import input_string


def unique_in_string(char14_string):
    if len(char14_string) != 14:
        return False
    for i, char_comp in enumerate(char14_string):
        for char in char14_string[i + 1 :]:
            if char_comp == char:
                return False
    return True


for i, char in enumerate(input_string[:-13]):
    char14_string = input_string[i : i + 14]
    unique_status = unique_in_string(char14_string=char14_string)
    if unique_status:
        print(char14_string)
        print(i + 14)
        break
