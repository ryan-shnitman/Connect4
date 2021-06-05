#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ processes a move by specified player on specified board """
    print('Player', player.checker + "'s", 'turn')
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print()
    print(board)
    if board.is_win_for(player.checker) == True:
        print('Player', player.checker, 'wins in', str(player.num_moves), 'moves.')
        print('Congratulations!')
        return True
    if board.is_win_for(player.checker) == False and \
       board.is_win_for(player.opponent_checker()) == False and \
       board.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ player subclass for an unintelligent AI player """

    def next_move(self, board):
        """ overrides inherrited next_move method; returns random column where player could validly move """
        options = [col for col in range(board.width) if board.can_add_to(col) == True]
        col = random.choice(options)
        self.num_moves += 1
        return col

