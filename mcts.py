# -*- coding: utf-8 -*-
"""mcts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U1h48UjoOUZmrg6JTj0nvTh-cAyenGe
"""

# mcts.py

import random


class GameRulesIF:
    def getPlayers(self):
        pass

    def getStartingPlayers(self):
        pass

    def getStartingNode(self, startingPlayer):
        pass


class GameNodeIF:
    def __init__(self, ruleset, moving_player, owning_player, parent_node):
        self.visits = 0
        self.scores = {}  # could be wins, could be cumulative scores
        self.ruleset = ruleset
        self.parent_node = parent_node
        self.moving_player = moving_player
        self.owning_player = owning_player

    def eval_uct(self, player):
        # TODO
        pass

    def is_terminal(self):
        # true if game should not continue past this point (could be a draw)
        pass

    def get_winner(self):
        pass

    def show(self):
        # this should have the board rep plus debug
        pass

    def show_small(self):
        pass

    def get_legal_moves(self):
        pass

    def apply_move(self, move_str):
        pass

    def get_key(self):
        pass


class PlayerIF:
    def __init__(self, player_name):
        self.player_name = player_name

    def make_move(self, node):
        pass
