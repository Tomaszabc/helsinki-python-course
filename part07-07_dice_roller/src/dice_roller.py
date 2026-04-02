# Write your solution here
from random import choice


def roll(die: str):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }

    return choice(dice[die])


def play(die1: str, die2: str, times: int):
    one_won = 0
    two_won = 0
    tie = 0

    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            one_won += 1
        elif roll1 < roll2:
            two_won += 1
        else:
            tie += 1

    return (one_won, two_won, tie)




# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)