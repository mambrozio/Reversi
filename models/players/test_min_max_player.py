from models.board import Board
from models.move import Move

class MinmaxPlayer:
    def __init__(self, color):
        self.color = color


    def play(self, board):
        print "OI"

        best_move = self.minmax(board, self.color, 0)

        return best_move

    def board_state(self, board, player_color):
        state = 0
        for line in range(1, 9):
            for col in range(1, 9):
                if board.board[line][col] == player_color:
                    temp_move = Move(line, col)
                    state += self.heuristic(temp_move)

        return state

    def max_move(self, board, player_color, depth):
        total_score = board.score()
        #print "entrei no max_move " + str(total_score[0]) + " " + str(total_score[1])
        if (total_score[0] + total_score[1]) == 64 or depth == 6:
            #return self.board_state(board, player_color)
            return None
        else:
            best_move_value = -1000
            best_move = None
            for m in board.valid_moves(player_color):
                new_board = board.get_clone()
                new_board.play(m, player_color)
                move = self.min_move(new_board, board._opponent(self.color), depth + 1)
                if move != None:
                    move_value = self.heuristic(move)
                    #print str(move_value) + " - max_move"
                    if (move_value > best_move_value):
                        best_move = move
                        best_move_value = move_value
                else:
                    best_move = m
                    best_move_value = self.heuristic(m)
            return best_move

    def min_move(self, board, player_color, depth):
        best_move_value = 1000
        best_move = None
        #print "entrei no min_move"
        for m in board.valid_moves(player_color):
            new_board = board.get_clone()
            new_board.play(m, player_color)
            move = self.max_move(new_board, board._opponent(self.color), depth + 1)
            if move != None:
                move_value = self.heuristic(move)
                #print str(move_value) + " - min_move"
                if (move_value > best_move_value):
                    best_move = move
                    best_move_value = move_value
            else:
                best_move = m
                best_move_value = self.heuristic(m)
        return best_move

    def minmax(self, board, player_color, depth):
        return self.max_move(board, self.color, depth)


    def heuristic(self, move):
        board_values = [100,  -1,   2,   5,   5,   6,  -1, 100,
                         -1,  -1,   8,   3,   3,   8,  -1,  -1,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          4,   3,   2,   0,   0,   2,   3,   4,
                          4,   3,   2,   0,   0,   2,   3,   4,
                          3,   7,   3,   2,   2,   3,   7,   3,
                         -1,  -1,   8,   3,   3,   8,  -1,  -1,
                        100,  -1,   2,   5,   5,   6,  -1, 100]
        #TODO deletar prints apos termino
        #print "[" + str(move.x) + ", " + str(move.y) + "]"

        #linha e coluna de 1 a 8!!!
        line = move.x - 1
        col = move.y - 1

        return board_values[(8 * line) + col]


    def get_best_move(self, moves):
        best_move = None
        best_move_value = -1000
        for move in moves:
            #check heuristic of that move
            move_value = self.heuristic(move)

            if best_move_value < move_value:
                best_move = move
                best_move_value = move_value

        return best_move
