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
