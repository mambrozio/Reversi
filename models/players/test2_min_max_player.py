from models.board import Board
from models.move import Move

class MinmaxPlayer:
    def __init__(self, color):
        self.color = color


    def play(self, board):
        print "OI TEST"

        best_move = self.minmax(board, self.color, 0)
        print "best_move: " + str(best_move)

        return best_move

    def board_value(self, board, player_color):
        game_value = 0
        for line in range(1, 9):
            for col in range(1, 9):
                if board.board[line][col] == player_color:
                    temp_move = Move(line, col)
                    game_value += self.heuristic(temp_move)

        return game_value

    def max_move(self, board, player_color, depth):
        g_over = self.gameover(board)
        if g_over:
            if g_over == 2: #Empate
                return 0
            multiplier = 2*(int(player_color > '@') - 0.5)
            return multiplier*g_over*1000000 #Numero muito grande
            
        if depth >= 4:
            return self.board_value(board,player_color)
            
        #i=0
        best_move_value = -1000000 #Numero muito pequeno
        for m in board.valid_moves(player_color):
            #fo = open("teste.txt", "a")
            #fo.write(str(depth) + " " + str(i) + " max move: " + str(m))
            #i += 1
            #raw_input()
            new_board = board.get_clone()
            new_board.play(m, player_color)
            #fo.write(str(new_board))
            #fo.close()
            value = self.min_move(new_board, board._opponent(self.color), depth + 1)
            if value > best_move_value:
                best_move_value = value
            if (depth == 0):
                best_move = m;
        if depth == 0:
            return best_move
        return best_move_value

    def min_move(self, board, player_color, depth):
        g_over = self.gameover(board)
        if g_over:
            if g_over == 2: #Empate
                return 0
            multiplier = 2*(int(player_color > '@') - 0.5)
            return multiplier*g_over*1000000 #Numero muito grande
            
        if depth >= 4:
            return self.board_value(board,player_color)

        #i = 0
        best_move_value = 1000000
        for m in board.valid_moves(player_color):
            #fo = open("teste.txt", "a")
            #fo.write(str(depth) + " " + str(i) + " min move: " + str(m))
            #i += 1
            new_board = board.get_clone()
            new_board.play(m, player_color)
            #fo.write(str(new_board))
            #fo.close()
            value = self.max_move(new_board, self.color, depth + 1)
            if value < best_move_value:
                best_move_value = value
        return best_move_value

    def minmax(self, board, player_color, depth):
        return self.max_move(board, self.color, depth)


    def heuristic(self, move):
        board_values = [100,   0,   6,   5,   5,   6,   0, 100,
                          0,   0,   8,   3,   3,   8,   0,   0,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          4,   3,   2,   1,   1,   2,   3,   4,
                          4,   3,   2,   1,   1,   2,   3,   4,
                          3,   7,   3,   2,   2,   3,   7,   3,
                          0,   0,   8,   3,   3,   8,   0,   0,
                        100,   0,   6,   5,   5,   6,   0, 100]
        #TODO deletar prints apos termino
        #print "[" + str(move.x) + ", " + str(move.y) + "]"

        #linha e coluna de 1 a 8!!!
        line = move.x - 1
        col = move.y - 1

        return board_values[(8 * line) + col]

    def gameover(self,board):
        #Retorna 1 se o branco ganhar e -1 se o preto ganhar.
        #0 se nao tiver gameover.
        #2 se for empate
        
        #Nao ha movimentos validos
        score = board.score()
        if (not board.valid_moves(self.color)) and (not board.valid_moves(board._opponent(self.color))):
            if score[0]==score[1]:
                return 2
            return int(2*int(score[0] > score[1]) - 0.5) #+1 se o branco ganhar ou -1 se o branco perder
        return 0 #Jogo continua!