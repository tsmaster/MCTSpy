# TODO

## Chess
The big aspiration is to implement chess. This might not be a huge
effort, as there are packages available that provide support for chess
board representations, calculating legal moves, etc.

One thing I've been curious to try is to build a parametrizable
evaluation function (e.g. queens are worth 12, rooks are worth 7,
board space d4 is worth 2 points if you have a piece on it, but 1
point for each piece you have that could capture a piece on it), and
then do a "tournament", using genetic algorithms to find more capable
parameter sets. I hope to track Elo ratings of the different
parameter sets to watch their progress. An early criterion of success
will be if one of the AIs can beat me.


## Rust
Even though this is currently completely implemented in Python, I want
to port to Rust, which will make it easier to deploy to Android and
Web.


## Human player (text)
Allowing a human player interface should be as easy as an input
prompt, validating moves against the legal move list, and maybe some
commands like "quit".


## Human player (GUI)
Rewriting the harness to be under a GUI loop might not be too hard. A
few pieces to do would be:

### Static Board Display (per game)
Each game will need to know how to draw the current configuration of
the board

### Move Animations (per game)
I will be able to give the GUI a starting board configuration, a
target board configuration, and the move that was made. This should
allow for pieces to animate on or off the board, pieces to move from
position to position, pieces to change (e.g. a pawn promoting into a
queen, or some other piece).

### Multi-threaded AI
It might make sense to put the AI on a separate thread, to allow the
UI to remain responsive during gameplay. This ends up not working well
for e.g. WASM targets.

### Timesliced AI
Rather than using OS threads, we can give the AI a small amount of
time to do its work, having it return to us so that we can update the
UI.

### Distributed AI
This is not so much a necessary feature of a GUI AI, but I have CPU
power around the house, what if, for each available move, I spawn off
workers on different worker nodes to find the best move(s), and then
merge them back at the center node?

