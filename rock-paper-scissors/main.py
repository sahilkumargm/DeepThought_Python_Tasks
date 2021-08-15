# Rock, Paper, Scissors console game
# Sahil Kumar
# On 15th August, 2021

import time
import random
import logic


def rpc(user_name):
    """
    Initilizes the game. Calls the logic.py module to execute the game.
    :param user_name: Accepts your name as the parameter
    :return: Nothing
    """

    # Names of the opponent for the user. Names are chosen randomly so that everytime the user plays, it's a new name.
    names = ["Maddie", "Paul", "Elizabeth"]
    comp_user = random.choice(names)
    welcome_message = f"\nHi {user_name}! Welcome to Rock, Paper, Scissors! I'm your opponent, {comp_user}. Let's play!"
    print(welcome_message)
    time.sleep(1)

    # Calling the logic.py module to execute the game
    game_logic = logic.rpc_logic("rock", "paper", "scissor")
    game_logic.main_logic()

    # Copying over the win values from the rpc_logic class to determine who finally won
    user_wins = game_logic.user_wins
    comp_wins = game_logic.comp_wins

    if user_wins == 3:
        print(f"{user_name_input} wins!")
    else:
        print(f"{comp_user} wins!")


user_name_input = input("Hey, what's your name? \n")

# Calling the function to start the game.
rpc(user_name_input)


