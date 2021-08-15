import random


class rpc_logic():
    def __init__(self, rock, paper, scissor):
        self.rock = rock
        self.paper = paper
        self.scissor = scissor
        self.moves = ["rock", "paper", "scissor"]
        self.comp_wins = 0
        self.user_wins = 0
        self.round_winner = 0

    def scoreboard(self):
        """
        Simply displays the current score
        :return: Nothing
        """
        print(f"You: {self.user_wins}\tYour opponent: {self.comp_wins}\n")


    def main_logic(self):
        """
        The main logic of the game - asks for the user's input, and compares it against a random choice by the
        computer and determines who won. :return: 0 (if user looses the round), 1 (if user wins the round),
        -1 (if game is tied)
        """
        while self.comp_wins < 3 and self.user_wins < 3:
            # print(f"{self.comp_wins}, {self.user_wins}")
            comp_input = random.choice(self.moves)
            user_input = input("Choose a move: 'rock','paper','scissors' \n")

            # The actual "meat" of the whole game:
            if user_input == "rock" and comp_input == "scissor":
                self.user_wins += 1
                print("rock beats scissors, you win this round\n")
                self.scoreboard()

            elif user_input == "rock" and comp_input == "paper":
                self.comp_wins += 1
                print("paper beats rock, you loose this round\n")
                self.scoreboard()

            elif user_input == "paper" and comp_input == "scissor":
                self.comp_wins += 1
                print("scissor cuts paper, you loose this round\n")
                self.scoreboard()

            elif user_input == "paper" and comp_input == "rock":
                self.user_wins += 1
                print("paper beats rock, you win this round\n")
                self.scoreboard()

            elif user_input == "scissor" and comp_input == "rock":
                self.comp_wins += 1
                print("rock beats scissors, you loose this round\n")
                self.scoreboard()

            elif user_input == "scissor" and comp_input == "paper":
                self.user_wins += 1
                print("scissors beats paper, you win this round\n")
                self.scoreboard()

            # Also serves as an exception handler for when the user doesn't enter one of the three choices.
            else:
                self.comp_wins += 0
                self.user_wins += 0
                print("Tie!\n")
                self.scoreboard()



