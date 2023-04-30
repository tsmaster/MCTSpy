import random

import mcts


class Harness:
    def __init__(self, ruleset):
        self.ruleset = ruleset
        self.players = {}

    def add_player(self, player_name, player):
        self.players[player_name] = player

    def play(self):
        starting_players = self.ruleset.getStartingPlayers()
        sp = random.choice(starting_players)
        print("{0} will start".format(sp))
        node = self.ruleset.getStartingNode(sp)

        while True:
            print("top of loop")
            node.show()

            node_player = node.moving_player
            print("{0} to move".format(node_player))
            m = self.players[node_player].make_move(node)
            print("{0} chose move {1}".format(node_player, m))

            new_node = node.apply_move(m)

            if new_node.is_terminal():
                print("done")
                print("final board:")
                new_node.show()
                w = new_node.get_winner()
                if w == "-":
                    print("draw")
                else:
                    print("{0} wins".format(w))

                break
            else:
                node = new_node
