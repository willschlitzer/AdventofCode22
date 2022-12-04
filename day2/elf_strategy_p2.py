# A - rock
# B - paper
# C - scissors

# X - rock / lose
# Y - paper / draw
# Z - scissors / win


def second_game_decider(opponent_play, outcome):
    if opponent_play == "A":
        if outcome == "X":
            return 0, "Z"
        elif outcome == "Y":
            return 3, "X"
        elif outcome == "Z":
            return 6, "Y"
    elif opponent_play == "B":
        if outcome == "X":
            return 0, "X"
        elif outcome == "Y":
            return 3, "Y"
        elif outcome == "Z":
            return 6, "Z"
    elif opponent_play == "C":
        if outcome == "X":
            return 0, "Y"
        elif outcome == "Y":
            return 3, "Z"
        elif outcome == "Z":
            return 6, "X"


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
    score_update, outcome = second_game_decider(opponent_play=game[0], outcome=game[1])
    total_score += score_update
    total_score += personal_play_score(your_play=outcome)

print(total_score)
