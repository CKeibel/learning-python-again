"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).

players = []

For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

if __name__=="__main__":
    players = [
        {"name": "Tom", "numbers": {1, 2, 3, 4, 5}},
        {"name": "Anne", "numbers": {6, 3, 1, 8, 9}}
    ]

    lottery_numbers = {2, 3, 6, 8, 9}

    res = players[0]['numbers'].intersection(lottery_numbers)
    numbers_right = len(res)
    print(f"Player {players[0]['name']} got {numbers_right} numbers right.")

    res = players[1]['numbers'].intersection(lottery_numbers)
    numbers_right = len(res)

    print(f"Player {players[1]['name']} got {numbers_right} numbers right.")
