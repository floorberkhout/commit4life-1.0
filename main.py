import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
import numpy as np

# importeer de gebruikte structuur
from board import Board
from random_algo import random_algo
from winning_row import winning_row
from palomaalgoritme import algoritme1


def main():

    board = Board("data/Rushhour9x9_5.csv")

    # move_count, time_elapsed = winning_row(board)    

    move_count, time_elapsed = random_algo(board)

    board.print_board()

    board.end_game(move_count, time_elapsed)


    
    



if __name__ == "__main__":
    main()