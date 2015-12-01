from models.board import Board
from models.move import Move

class HeuristcvaluePlayer:
    def __init__(self, color):
        self.color = color


    def play(self, board):
        #get array of valid moves
        moves = board.valid_moves(self.color)

        #see which move has the best value
        best_move = self.get_best_move(moves)

        return best_move


    def heuristic(self, move):
        board_values = [100,  -1,   2,   5,   5,   6,  -1, 100,
                         -1,   3,   1,   1,   1,   1,   3,  -1,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          4,   1,   2,   0,   0,   2,   1,   4,
                          4,   1,   2,   0,   0,   2,   1,   4,
                          3,   7,   3,   2,   2,   3,   7,   3,
                         -1,   3,   1,   1,   1,   1,   3,  -1,
                        100,  -1,   2,   5,   5,   6,  -1, 100]
        #TODO deletar prints apos termino
        print "[" + str(move.x) + ", " + str(move.y) + "]"

        #linha e coluna de 1 a 8!!!
        linha = move.x - 1
        coluna = move.y - 1

        return board_values[(8 * linha) + coluna]


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
