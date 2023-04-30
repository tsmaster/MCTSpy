# MCTSpy

An implementation of Monte Carlo Tree Search (MCTS) in Python. I
aspire to implement several games that will use MCTS as an AI player,
including:

- Connect 2 (toy game, only for testing)
- Tic Tac Toe (3x3 board)
- Tic Tac Toe (4x4 board)
- 3d Tic Tac Toe (3x3x3 board)
- Connect 4 (7x6 board)
- Awari/Mancala
- Small Dots and Boxes (3x3 dots)
- Checkers
- Cromwell's Checkers (no kings)
- Small Checkers (6x6 board)
- Chess

## Architecture

The current architecture is broken up into a few pieces:

### GameNodeIF

The Game Node Interface (GameNodeIF) classes are game-specific
descriptions of game state, including positions of all pieces on the
board. There may be other information, including history - for
example, in chess, it is important to keep track of whether the kings
and rooks have moved, to know if castling is available.

GameNodes are responsible for knowing if they are a winning/losing
node, and for which player. They are responsible for creating a new
game node when given a move to "apply" to themselves.


### GameRulesIF

The Game Rules Interface (GameRulesIF) classes provide the ability to
start a game, including what player names are supported, and what
player(s) can go first, along with the initial BoardNode.


### PlayerIF

The layer Interface is responsible for taking a GameNode and
returning a move. All annotation of board states are managed within
the Player and its subordinate classes.

Note that a Player is not tied to the game, which means that it is
possible to write a general AI that does not know what game it's
playing, only using the GameNode interface to determine if a position
has been won. This is probably insufficient for bigger games, where a
board evaluation function will be required to understand progress.


### Harness

I have implemented a Harness class that takes a GameRules object and
some number (so far, two) AI Player objects, and calls the player
objects in turn to make moves until there is a winner.