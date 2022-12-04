# A - rock
# B - paper
# C - scissors

# X - rock
# Y - paper
# Z - scissors


def first_game_decider(opponent_play, your_play):
    if opponent_play == "A":
        if your_play == "X":
            return 3
        elif your_play == "Y":
            return 6
        elif your_play == "Z":
            return 0
    elif opponent_play == "B":
        if your_play == "X":
            return 0
        elif your_play == "Y":
            return 3
        elif your_play == "Z":
            return 6
    elif opponent_play == "C":
        if your_play == "X":
            return 6
        elif your_play == "Y":
            return 0
        elif your_play == "Z":
            return 3


def personal_play_score(your_play):
    if your_play == "X":
        return 1
    elif your_play == "Y":
        return 2
    elif your_play == "Z":
        return 3


game_list = []

with open("playlist.txt", "r") as f:
    for line in f:
        game_list.append([line.split()[0], line.split()[1]])

total_score = 0
for game in game_list:
    total_score += personal_play_score(your_play=game[1])
    total_score += first_game_decider(opponent_play=game[0], your_play=game[1])

print(total_score)
