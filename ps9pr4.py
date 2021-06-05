#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ player subclass that intelligently selects moves """

    def __init__(self, checker, tiebreak, lookahead):
        """ constructor for AIPlayer object """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns string representation of AIPlayer object """
        s = super().__repr__()
        s += ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """ returns column index of max score in list of column scores """
        choices = [col for col in scores if col == max(scores)]
        choices = []
        n = 0
        for col in scores:
            if col == max(scores):
                choices += [n]
            n += 1
        if self.tiebreak == 'LEFT':
            return choices[0]
        if self.tiebreak == 'RIGHT':
            return choices[-1]
        else:
            return random.choice(choices)
        
    def scores_for(self, board):
        """ returns scores for columns in board for specified lookahead """
        scores = [0] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_scores = opponent.scores_for(board)
                if max(opponent_scores) == 100:
                    scores[col] = 0
                elif max(opponent_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """ overrides inheritted next_move and returns AI player's best move """
        col = self.max_score_column(self.scores_for(board))
        self.num_moves += 1
        return col
                
