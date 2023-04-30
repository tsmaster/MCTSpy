import random

import mcts


class Connect2GameRules(mcts.GameRulesIF):
    def getPlayers(self):
        return ["X", "O"]

    def getStartingPlayers(self):
        return ["X", "O"]

    def getStartingNode(self, startingPlayer):
        return Connect2GameNode(self, startingPlayer, None, None)

    def otherPlayer(self, player_string):
        if player_string == "X":
            return "O"
        else:
            return "X"


class Connect2GameNode(mcts.GameNodeIF):
    def __init__(self, ruleset, moving_player, owning_player, parent_node):
        super().__init__(ruleset, moving_player, owning_player, parent_node)
        self.cells = [".", ".", ".", "."]

    def show(self):
        print(self.cells)
        # print("{0} to move". format(self.moving_player))

    def get_legal_moves(self):
        moves_list = []
        for i, _ in enumerate(self.cells):
            if self.is_empty(i):
                moves_list.append(str(i + 1))
        return moves_list

    def is_empty(self, posn):
        return self.cells[posn] == "."

    def apply_move(self, move_str):
        idx = int(move_str)
        assert idx > 0
        assert idx <= len(self.cells)

        idx = idx - 1
        assert self.is_empty(idx)

        new_moving_player = self.ruleset.otherPlayer(self.moving_player)
        new_owning_player = self.moving_player

        new_node = Connect2GameNode(
            self.ruleset, new_moving_player, new_owning_player, self
        )
        new_node.cells = self.cells[:]

        new_node.cells[idx] = self.moving_player

        return new_node

    def is_terminal(self):
        w = self.get_winner()
        if w != "-":
            return True

        # check for an empty space
        for val in self.cells:
            if val == ".":
                return False
        return True

    def get_winner(self):
        for i in range(len(self.cells) - 1):
            j = i + 1
            if (self.cells[i] == self.cells[j]) and (self.cells[i] != "."):
                return self.cells[i]
        return "-"

    def get_key(self):
        s = "".join(self.cells)

        return s
