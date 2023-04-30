import mcts

import random


class RandomPlayer(mcts.PlayerIF):
    def make_move(self, node):
        moves = node.get_legal_moves()
        return random.choice(moves)


class RandomRolloutPlayer(mcts.PlayerIF):
    def __init__(self, player_name, num_rollouts, max_moves):
        super().__init__(player_name)
        self.num_rollouts = num_rollouts
        self.max_moves = max_moves

    def rollout(self, node, max_moves):
        while True:
            if node.is_terminal() or max_moves <= 0:
                return node.get_winner()
            moves = node.get_legal_moves()
            m = random.choice(moves)
            new_node = node.apply_move(m)
            node = new_node
            max_moves = max_moves - 1

    def make_move(self, node):
        reward_dict = {}
        for m in node.get_legal_moves():
            next_node = node.apply_move(m)
            reward_dict[m] = 0
            for i in range(self.num_rollouts):
                rw = self.rollout(next_node, self.max_moves)
                # print ("in rollout, found win for", rw)
                if rw == self.player_name:
                    reward_dict[m] = reward_dict.get(m, 0) + 1
                elif rw == "-":
                    reward_dict[m] = reward_dict.get(m, 0) + 0.5

        best_move = None
        best_wins = 0

        # print("rollout results:", reward_dict)

        for k, v in reward_dict.items():
            if (best_move is None) or (v > best_wins):
                best_move = k
                best_wins = v

        return best_move
