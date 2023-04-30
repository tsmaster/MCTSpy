# tic tac toe test

import mcts
import harness
import tictactoe
import randomplayers
import mctsplayer

ticTacToeRuleset = tictactoe.TicTacToeGameRules()
#xplayer = randomplayers.RandomPlayer('X')
#xplayer = randomplayers.RandomRolloutPlayer("X", 100, 8)
xplayer = mctsplayer.MCTSPlayer("X", 5, 8)
#oplayer = randomplayers.RandomRolloutPlayer("O", 100, 8)
oplayer = mctsplayer.MCTSPlayer("O", 5, 8)

h = harness.Harness(ticTacToeRuleset)
h.add_player("X", xplayer)
h.add_player("O", oplayer)
#h.getStartingPlayers = lambda x: ["X"]

h.play()
