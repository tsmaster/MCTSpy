import time
import random

import mcts
import mctsmath


class MCTSPlayer(mcts.PlayerIF):
    def __init__(self, player_name, move_seconds, max_moves):
        super().__init__(player_name)

        self.move_seconds = move_seconds
        self.max_moves = max_moves

        self.node_dict = {}

    def rollout(self, node_key, max_moves):
        node = self.node_dict[node_key].node
        
        while True:
            if node.is_terminal() or max_moves <= 0:
                return node.get_winner()
            moves = node.get_legal_moves()
            m = random.choice(moves)
            new_node = node.apply_move(m)
            node = new_node
            max_moves = max_moves - 1

    def get_or_create_node_wrapper(self, key, node, opt_parent_key, player, history):
        if not (key in self.node_dict):
            self.node_dict[key] = MCTSNodeWrapper(node, opt_parent_key, player, history)
        return self.node_dict[key]

    def get_node_wrapper(self, key):
        assert (key in self.node_dict)
        
        return self.node_dict[key]

    def make_move(self, root_node):
        # clearing out memory FOR NOW?
        self.node_dict = {}
        start_time = time.time()
        print("MCTS Player {0} starting to make move".format(self.player_name))
        root_node.show()

        root_key = root_node.get_key()
        #print("key:", root_key)

        root_node_wrapper = self.get_or_create_node_wrapper(root_key, root_node, None, self, "")

        while True:
            time_now = time.time()

            if time_now - start_time >= self.move_seconds:
                break

            #print("time remaining at top of loop:", (start_time+ self.move_seconds) - time_now)

            #for k,v in self.node_dict.items():
            #    print("node k:{0} p:{3}  visits:{1} wins:{2}".format(k, v.visits, v.wins, v.parent_key))
            #print("---")
            
            # select a node
            child_key = self.select(root_key)
            #print ("selected key:", child_key)

            # expand (if possible)
            new_leaf_key = self.expand(child_key)
            #print ("new leaf key:", new_leaf_key)

            if (new_leaf_key is None):
                child_node_wrapper = self.get_node_wrapper(child_key)
                child_node = child_node_wrapper.node
                
                if child_node.is_terminal():
                    #print("reached a terminal node")
                    #child_node.show()
                    w = child_node.get_winner()
                    #print("winner:", w)
                    self.backprop(w, child_key, root_key)
                else:
                    print("no children, wtf?")
                    assert(False)
            else:
                # rollout
                winner = self.rollout(new_leaf_key, self.max_moves)

                # backprop
                self.backprop(winner, new_leaf_key, root_key)

        # pick child with greatest number of visits

        best_visit_move = None
        most_visits = None

        #best_winfrac_move = None
        #best_winfrac = None

        for mv, ck in root_node_wrapper.children_keys.items():
            child_wrapper = self.get_node_wrapper(ck)

            my_wins = child_wrapper.wins.get(self.player_name, 0)
            my_win_frac = float(my_wins) / child_wrapper.visits
            
            print("considering move {0} with visits {1} and wins {2}".format(
                mv,
                child_wrapper.visits,
                child_wrapper.wins))
                
            if best_visit_move is None or child_wrapper.visits > most_visits:
                best_visit_move = mv
                most_visits = child_wrapper.visits

            #if best_winfrac_move 

        

        return best_visit_move

    def select(self, node_key):
        # if this is a leaf node (no children), return node
        # if one of the children has not been visited, return that child
        # else, use UCT to select the best child

        #print("at top of select, looking for", node_key)

        while True:
            #print("at top of select loop, looking for", node_key)
            node_data = self.node_dict[node_key]

            #print("got node_data")
            if node_data.is_leaf:
                #print("node is leaf")
                return node_key

            #print("node is not leaf!")

            best_node_key = None

            # if any child has 0 visits, randomly pick from them
            # else, use UCT to choose

            no_visit_child_keys = []

            best_uct = None
            best_move = None

            #print("children of node_data")
            #for k,v in node_data.children_keys.items():
            #    print(k,v)
        
            for mv, child_key in node_data.children_keys.items():
                child_node_wrapper = self.get_node_wrapper(child_key)

                parent_visit_count = 0
                if child_node_wrapper.parent_key != None:
                    parent_node_wrapper = self.get_node_wrapper(child_node_wrapper.parent_key)
                    parent_visit_count = parent_node_wrapper.visits
                
                #print("visits:", child_node_wrapper.visits)
                if ((child_node_wrapper.visits == 0) or
                    (parent_visit_count == 0)):
                    no_visit_child_keys.append(child_key)
                else:
                    node_player = child_node_wrapper.node.moving_player
                    node_owner = child_node_wrapper.node.owning_player

                    if node_owner == '-':
                        win_count = 0
                    else:
                        win_count = (child_node_wrapper.wins.get(node_owner, 0) +
                                     child_node_wrapper.wins.get('-', 0) * 0.5)
                    
                    #print("UCT", win_count, child_node_wrapper.visits, parent_visit_count)
                    
                    uct = mctsmath.calc_uct(win_count,
                                            child_node_wrapper.visits,
                                            mctsmath.EXPLORE_CONSTANT,
                                            parent_visit_count)
                    #print("UCT", uct)
                    if ((best_move is None) or
                        (uct > best_uct)):
                        best_uct = uct
                        best_move = child_key
    
            if len(no_visit_child_keys) > 0:
                ck = random.choice(no_visit_child_keys)
                child_node_wrapper = self.get_node_wrapper(ck)
                #print("returning {0} that should have no visits".format(ck))
                #print("cnw visits:", child_node_wrapper.visits)
                #print("cnw is leaf?:", child_node_wrapper.is_leaf)
                return ck
            
            node_key = best_move


    def expand(self, node_key):
        # take a node that has not been expanded (TODO - understand)
        # and make empty child nodes, and return a random one

        # foreach move from node, add empty child

        assert(node_key in self.node_dict)

        node_wrapper = self.node_dict[node_key]

        assert(node_wrapper.is_leaf)

        node = node_wrapper.node

        #print("in expand, starting from node", node)
        #node.show()

        if node.is_terminal():
            # no children
            #print("returning none from expand because node is terminal")
            return None

        # not a leaf anymore!
        node_wrapper.is_leaf = False

        new_node_keys = []

        nw_hist = node_wrapper.history
        
        for mv in node.get_legal_moves():
            #print("in expand, working with move", mv)
            child_node = node.apply_move(mv)
            child_history = nw_hist + mv
            child_node_key = child_node.get_key() + '|' + child_history
            new_node_keys.append(child_node_key)

            #print("child node key:", child_node_key)            
            child_node_wrapper = self.get_or_create_node_wrapper(child_node_key, child_node, node_key, self, child_history)
            
            # put children info into node_wrapper
            node_wrapper.children_keys[mv] = child_node_key
        
        if len(new_node_keys) == 0:
            return None

        return random.choice(new_node_keys)

    def backprop(self, winner, cur_key, root_key):
        # for each node from new_leaf up to root node, add the winner value

        while True:
            cur_node_wrapper = self.node_dict[cur_key]
            cur_node_wrapper.wins[winner] = cur_node_wrapper.wins.get(winner,0) + 1
            cur_node_wrapper.visits += 1

            if cur_key == root_key:
                return
            
            cur_key = cur_node_wrapper.parent_key


class MCTSNodeWrapper:
    """
    This holds the win and visited count for a node
    it should hold the moves
    """
    def __init__(self, node, opt_parent_key, player, history):
        self.wins = {}
        self.visits = 0
        self.node = node
        self.key = node.get_key() + '|' + history
        self.parent_key = opt_parent_key
        self.player = player
        self.history = history
        #print("making data for", self.key)

        # maps from move to child key
        self.children_keys = {}

        self.is_leaf = True

        for m in node.get_legal_moves():
            self.children_keys[m] = None

            #print("storing move {0}".format(m))
    
