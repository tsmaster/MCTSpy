ruleset = Connect2GameRules()
# print(dir(ruleset))
start_node = ruleset.getStartingNode("X")
print(start_node)
start_node.show()
print(start_node.get_legal_moves())

node_1 = start_node.apply_move("2")
# print("node 1:", node_1)
node_1.show()

node_2 = node_1.apply_move("1")
node_2.show()

node_3 = node_2.apply_move("3")
node_3.show()

print("is terminal?", node_3.is_terminal())
print("winner:", node_3.get_winner())
