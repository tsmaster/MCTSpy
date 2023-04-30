# tictactoe

import mcts


class TicTacToeGameRules(mcts.GameRulesIF):
    def getPlayers(self):
        return ["X", "O"]

    def getStartingPlayers(self):
        return ["X", "O"]

    def getStartingNode(self, startingPlayer):
        return TicTacToeGameNode(self, startingPlayer, None, None)

    def otherPlayer(self, player_string):
        if player_string == "X":
            return "O"
        else:
            return "X"


class TicTacToeGameNode(mcts.GameNodeIF):
    def __init__(self, ruleset, moving_player, owning_player, parent_node):
        super().__init__(ruleset, moving_player, owning_player, parent_node)
        self.cells = [".", ".", ".", ".", ".", ".", ".", ".", "."]

    def show(self):
        print(self.cells[:3])
        print(self.cells[3:6])
        print(self.cells[6:])
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

        new_node = TicTacToeGameNode(
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
        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for player in self.ruleset.getPlayers():
            for row in wins:
                foundNot = False
                for square in row:
                    if self.cells[square] != player:
                        foundNot = True
                        break
                if not foundNot:
                    return player
        return "-"

    def get_key(self):
        s = "".join(self.cells)
        return s
