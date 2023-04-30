import math

import mcts

EXPLORE_CONSTANT = 1.4

# MCTS
def calc_uct(win_count, visit_count, explore_constant, parent_visit_count):
    if visit_count == 0:
        return None
    win_ratio = win_count / float(visit_count)
    return win_ratio + explore_constant * math.sqrt(
        math.log(parent_visit_count) / float(visit_count)
    )


if __name__ == "__main__":
    win_count = 2
    visit_count = 4
    parent_visit_count = 6

    print(calc_uct(win_count, visit_count, EXPLORE_CONSTANT, parent_visit_count))
