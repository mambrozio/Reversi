# README #

Work assignment for Artificial Inteligence class in 2015/2. DCC/UFRJ

Make a working AI player to compete against the AI of other groups.

Students: Matheus Ambrozio and Matheus Galvez


### Base of the project ###

As requested, the base of the game was already done in python. We only had to write the players.

* [Base project](https://github.com/victorlcampos/TabuleiroOthello)


### Heuristics ###

* Heuristic 1 - Board positions have different values;
* Heuristic 2 - Number of pieces owned;
* Heuristic 3 - Minimize opponents moves;
* Heuristic 4 - Mixed heuristics. Uses heuristics 1 or 3, according to some condition.


### Players ###

We wrote four players. All of them are based on the minimax algorithm using the alpha-beta pruning for improved speeds and greater depth during the search. The difference is on the board evaluation functions (the heuristics)

* [Player - Heuristic 1](https://github.com/mambrozio/Reversi/blob/master/models/players/table_minimax_alpha_beta_player.py)
* [Player - Heuristic 2](https://github.com/mambrozio/Reversi/blob/master/models/players/pieces_quantity_alpha_beta_player.py)
* [Player - Heuristic 3](https://github.com/mambrozio/Reversi/blob/master/models/players/minimize_moves_player.py)
* [Player - Heuristic 4](https://github.com/mambrozio/Reversi/blob/master/models/players/mixed_heuristic_player.py)
