import random
from minimax_algo import minimax

class HumanPlayer:
    def __init__(self, letter):
        letter = letter.upper()
        if letter not in ["X", "O"]:
            raise ValueError("Invalid symbol! Player must choose either 'X' or 'O'.")
        self.letter = letter

    def get_move(self, board):
        valid_char = False
        val = None
        while not valid_char:
            pos = input(f"Its {self.letter} turn! Please enter the position from 0 to 8: ")
            try:
                val = int(pos)
                if val not in range(9) or board.state[val] != " ":
                    raise ValueError
                valid_char = True
            except ValueError:
                print("Wrong Value, please enter a valid empty position from 0 to 8")
        return val