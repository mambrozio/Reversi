from models.board import Board
from models.move import Move

"""@package players
Documentation for the minimax with alpha-beta pruning.
"""

class Minimax1Player:
    """Documentation for the minimax with alpha-beta pruning AI player.

    This class is the implementation of the minimax algorithm with alpha-beta pruning
    for improved speed and greater depth search.
    """
    import random

    def __init__(self, color):
        """Constructor."""
        self.color = color
        self.max_depth = 4
        #self.max_pruned = 0 #debug
        #self.min_pruned = 0 #debug


    def play(self, board):
        """This is the function called by the board controller. Returns a Move."""

        # Everything commented on this function is for debugging purposes
        #import time

        print "Minimax Player with alpha-beta pruning. Heuristic 1 (table). Matheus Ambrozio and Matheus Galvez."

        #start = time.clock()

        best_move = self.minimax(board, self.color, 0)

        #elapsed = time.clock()
        #elapsed = elapsed - start

        #print "Time spent finding the best move: " + str(elapsed)
        #print "best_move (play): " + str(best_move)
        #print "pruned in max: " + str(self.max_pruned) + " | pruned in min: " + str(self.min_pruned)
        #self.max_pruned = 0
        #self.min_pruned = 0

        return best_move


    def board_value(self, board, player_color):
        """This function returns the value of the board received as argument.
        It is the sum of all positions that player_color has minus the sum of
        positions that the opposition has. Blank positions do not count.
        """
        game_value = 0
        for line in range(1, 9):
            for col in range(1, 9):
                temp_move = Move(line, col)
                multiplier = 0
                if board.board[line][col] == self.color:
                    multiplier = 1
                if board.board[line][col] == board._opponent(self.color):
                    multiplier = -1
                game_value = game_value + (multiplier * self.heuristic(temp_move))
        return game_value


    def max_move(self, board, player_color, depth, alpha, beta):
        """This is the max part of the alpha-beta pruning. It plays every valid
        move available for player_color (this player) until the game is over, if a move ends the game
        or the depth is reached. It calls the min part of the alpha-beta algorithm.
        During the recursive part, the return value (integer) of this function is the current best value.
        If depth is 0, meaning the end of the recursive part, it returns the best move (Move object)
        """
        # Checking if game is over and returning -1000000 for a loss, 1000000 for a win and 0 for a tie.
        g_over = self.gameover(board)
        if g_over:
            if g_over == 2: # tie
                return 0
            multiplier = 2 * (int(player_color > '@') - 0.5) # this makes multiplier -1 for a loss and +1 for a win
            return multiplier * g_over * 1000000 # very large number

        # Reached maximum depth for recursion
        if depth >= self.max_depth:
            return self.board_value(board,player_color)

        best_move_value = -1000000 # very small number
        best_move = None

        # Main loop. Check valid moves and call min for each move that can be made.
        for m in board.valid_moves(player_color):
            new_board = board.get_clone()
            new_board.play(m, player_color)

            # this checks if the current move ends the game by capturing all of the opponent's pieces.
            # if this happens, make this move.
            if depth == 0:
                new_board_score = new_board.score()
                if self.color == Board.WHITE:
                    if new_board_score[1] == 0:
                        best_move = m
                        break
                else:
                    if new_board_score[0] == 0:
                        best_move = m
                        break

            # Calls the min part of the algorithm.
            value = self.min_move(new_board, board._opponent(self.color), depth + 1, alpha, beta)

            # This updates the alpha value and the best move if the depth is 0
            if value > best_move_value:
                best_move_value = value
                if (depth == 0):
                    best_move = m;
            if (depth == 0) and (value == best_move_value) and (not best_move):
                best_move = m

            if value >= beta: # pruning
                #self.max_pruned += 1 #debug
                return value

            if value > alpha:
                alpha = value

        # Base of recursion. Returns the best move (Move object)
        if depth == 0:
            return best_move # returns the best move to minimax()

        # Return value of the recursive part of this algorithm.
        return best_move_value


    def min_move(self, board, player_color, depth, alpha, beta):
        """This is the min part of the alpha-beta pruning. It plays every valid
        move available for player_color (oppenent) until the game is over, if a move ends the game
        or the depth is reached. It calls the max part of the alpha-beta algorithm.
        Return value (integer) of this function is the current best value (beta).
        Very similar with the max function.
        """
        # Checking if game is over and returning -1000000 for a loss, 1000000 for a win and 0 for a tie.
        g_over = self.gameover(board)
        if g_over:
            if g_over == 2: # tie
                return 0
            multiplier = 2 * (int(player_color > '@') - 0.5)  # this makes multiplier -1 for a loss and +1 for a win
            return multiplier * g_over * 1000000 # very large number

        # Reached maximum depth for recursion
        if depth > self.max_depth:
            return self.board_value(board,self.color)

        best_move_value = 1000000 # very large number

        # Main loop. Check valid moves and call max for each move that can be made.
        for m in board.valid_moves(player_color):
            new_board = board.get_clone()
            new_board.play(m, player_color)

            value = self.max_move(new_board, self.color, depth + 1,alpha,beta)

            if value < best_move_value:
                best_move_value = value

            if value <= alpha: # pruning
                #self.min_pruned += 1 #debug
                return value

            if value < beta:
                beta = value

        return best_move_value


    def minimax(self, board, player_color, depth):
        """Wrapper function to call max and get the best move."""
        return self.max_move(board, self.color, 0, -10000000, 10000000)


    def heuristic(self, move):
        """This function returns the value of the move, according to the heuristic table below:
        100,   0,   6,   5,   5,   6,   0, 100
          0,   0,   8,   3,   3,   8,   0,   0
          3,   7,   3,   2,   2,   3,   7,   3
          4,   3,   2,   1,   1,   2,   3,   4
          4,   3,   2,   1,   1,   2,   3,   4
          3,   7,   3,   2,   2,   3,   7,   3
          0,   0,   8,   3,   3,   8,   0,   0
        100,   0,   6,   5,   5,   6,   0, 100
        """
        board_values = [100,   0,   6,   5,   5,   6,   0, 100,
                          0,   0,   8,   3,   3,   8,   0,   0,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          4,   3,   2,   1,   1,   2,   3,   4,
                          4,   3,   2,   1,   1,   2,   3,   4,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          0,   0,   8,   3,   3,   8,   0,   0,
                        100,   0,   6,   5,   5,   6,   0, 100]

        line = move.x - 1
        col = move.y - 1

        return board_values[(8 * line) + col]


    def gameover(self,board):
        """This function returns +1 if white player wins, -1 if black player wins,
        0 if game is not over and +2 if game is a tie
        """
        # No more valid moves
        score = board.score()
        if (not board.valid_moves(self.color)) and (not board.valid_moves(board._opponent(self.color))):
            if score[0]==score[1]:
                return 2 # tie
            return int(2 * int(score[0] > score[1]) - 0.5) # +1 if white player wins, -1 if black player wins

        return 0 # game goes on!
