#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    def __init__(self, checker):
        """ constructs player object with specified checker and 0 number of moves """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns string representation of player object """
        s = 'Player ' + self.checker
        return s

    def opponent_checker(self):
        """ returns the opponent's checker """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ asks user for column and returns column if valid; increments num_moves attribute """
        col = int(input('Enter a column: '))
        while board.can_add_to(col) == False:
            print('Try again!')
            col = int(input('Enter a column: '))
        self.num_moves += 1
        return col
