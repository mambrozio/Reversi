class GreedyPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.getNearestCorner(board)

  def getNearestCorner(self, board):
    max = 0
    retMove = None
    moves = board.valid_moves(self.color)
    max_depth = 6
    if len(moves) > 5:
        max_depth = 4
    if len(moves) > 10:
        max_depth = 3

    for move in moves:
        new_board = board.get_clone()
        new_board.play(move, self.color)
        score = self.greedy(new_board, 1, max_depth)
        if score is None:
            continue
        # print "score: " + repr(score)
        if score > max:
            max = score
            retMove = move
    if retMove is None:
        # print "escolhendo jogada sem entrar na arvore"
        for move in moves:
            new_board = board.get_clone()
            new_board.play(move, self.color)
            if self.color == board.WHITE:
                score = board.score()[0]
            else:
                score = board.score()[1]
            ## print "score: " + repr(score)
            if score > max:
                max = score
                retMove = move
    return retMove

  def get_opponent(self, board):
    if self.color == board.WHITE:
        return board.BLACK
    else:
        return board.WHITE

  def greedy(self, board, depth, max_depth):
    max = 0
    retMove = None

    # print "depth " + repr(depth)

    #caso base
    if depth == max_depth:
        # print "retornando score da board para max depth"
        if self.color == board.WHITE:
            return board.score()[0]
        else:
            return board.score()[1]

    #atribui player color
    player_color = self.color
    if depth % 2 == 1:
        player_color = self.get_opponent(board)

    moves = board.valid_moves(player_color)

    for move in moves:
        new_board = board.get_clone()

        #faz jogada
        new_board.play(move, player_color)

        score = self.greedy(new_board, depth + 1, max_depth)
        # print "score: " + repr(score) + " max: " + repr(max) + " retMove: " + repr(retMove)
        if score is None:
            continue

        if score > max:
            max = score
            retMove = move

    # print "depth " + repr(depth)

    if retMove is None:
        # print "retornando score do pai"
        if self.color == board.WHITE:
            return board.score()[0]
        else:
            return board.score()[1]
    return score
