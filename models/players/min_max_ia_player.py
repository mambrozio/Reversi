from models.board import Board
from models.move import Move

class MinMaxIAPlayer:
    def __init__(self, color):
        self.color = color


    def play(self, board):
        #get array of valid moves
        moves = board.valid_moves(self.color)

        #see which move has the best value
        best_move = None
        best_move_value = -1000
        for move in moves:
            #check heuristic of that move
            move_value = self.heuristic(move)

            if best_move_value < move_value:
                best_move = move
                best_move_value = move_value

        return best_move

        # while move not in board.valid_moves(self.color):
        #     print "Movimento invalido.Insira um valido"
        #     print board
        #     rowInp = int(raw_input("Linha: "))
        #     colInp = int(raw_input("Coluna: "))
        #     move = Move(rowInp, colInp)
        # return move


    def heuristic(self, move):
        board_values = [100,  -1,   2,   5,   5,   6,  -1, 100,
                         -1,   3,   1,   1,   1,   1,   3,  -1,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          4,   1,   2,   0,   0,   2,   1,   4,
                          4,   1,   2,   0,   0,   2,   1,   4,
                          3,   7,   3,   2,   2,   3,   7,   3,
                         -1,   3,   1,   1,   1,   1,   3,  -1,
                        100,  -1,   2,   5,   5,   6,  -1, 100]

        print move.x
        print move.y
        #linha e coluna de 1 a 8!!!
        linha = move.x - 1
        coluna = move.y - 1

        return board_values[(8 * linha) + coluna]
