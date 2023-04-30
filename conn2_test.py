import mcts
import harness
import conn2
import randomplayers

import mctsplayer

connect2Ruleset = conn2.Connect2GameRules()

# xplayer = randomplayers.RandomRolloutPlayer('X', 6, 5)
xplayer = mctsplayer.MCTSPlayer("X", 5, 5)
oplayer = randomplayers.RandomRolloutPlayer("O", 4, 5)

h = harness.Harness(connect2Ruleset)
h.add_player("X", xplayer)
h.add_player("O", oplayer)
h.getStartingPlayers = lambda x: "X"

h.play()
