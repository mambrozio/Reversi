# README #

Work assignment for Artificial Inteligence class in 2015/2. DCC/UFRJ


### Base of the project ###

As requested, the base of the game was already done in python. We only had to write the players.

* [Base project](https://github.com/victorlcampos/TabuleiroOthello)


### Heuristics ###

* Heuristic 1 - table
* Heuristic 2 - pieces
* Heuristic 3 - minimize
* Heuristic 4 - mixed


### Players ###

We wrote four players. All of them are based on the minimax algorithm using the alpha-beta pruning for improved speeds and greater depth during the search. The difference is on the board evaluation functions (the heuristics)

* [Player - Heuristic 1](http://github.com/mambrozio/Othello/blob/master/models/players/table_minimax_alpha_beta_player.py)
* [Player - Heuristic 2](http://github.com/mambrozio/Othello/blob/master/models/players/pieces_quantity_alpha_beta_player.py)
* [Player - Heuristic 3](http://github.com/mambrozio/Othello/blob/master/models/players/minimize_moves_player.py)
* [Player - Heuristic 4](http://github.com/mambrozio/Othello/blob/master/models/players/mixed_heuristic_player.py)


