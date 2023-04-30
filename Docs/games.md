# Games

MCTS seems reasonably well fit to a lot of 2-player, full information,
turn-based games. It's probably usable for at least some games beyond
that, as well.

## Aspirational List

Some of the games I would like to implement a game description of, if
not a custom AI for, include:

- Checkers
- Chess
- Connect 4
- Mancala
- Dots and Boxes (3x3 dots)
- Nim

## Currently Implemented Games

### Connect 2

This is not a game for humans to play, but it is useful as a stepping
stone to verify the AI's implementation. As implemented, the board is
a 1x4 rectangle of spots, and the players take turns placing a stone
in a spot. A player wins if any two of their stones connect. It is
clear to a human player that spaces 2 or 3 are winning first moves, as
each has two neighboring spaces, so whatever the second player plays,
the first player wins on their second move.


### Tic Tac Toe

Another game that most humans do not play after some familiarity -
perfect play leads to a draw.

Once I got this game working with the MCTS AI player, I was surprised
that there is exactly one game flow that ever gets played (discarding
rotations and reflections).