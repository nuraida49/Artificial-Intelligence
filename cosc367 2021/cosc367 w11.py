import math
def max_value(tree):
    if type(tree) != list:
        return tree
    else:
        utility = float("-inf")
        for node in tree:
            utility = max(utility, min_value(node))
    return utility

def min_value(tree):
    if type(tree) != list:
        return tree
    else:
        utility = float("inf")
        for node in tree:
            utility = min(utility, max_value(node))
    return utility

#game_tree = 3

#print("Root utility for minimiser:", min_value(game_tree))
#print("Root utility for maximiser:", max_value(game_tree))

#game_tree = [1, 2, 3]

#print("Root utility for minimiser:", min_value(game_tree))
#print("Root utility for maximiser:", max_value(game_tree))

#game_tree = [1, 2, [3]]

#print(min_value(game_tree))
#print(max_value(game_tree))

#game_tree = [[1, 2], [3]]

#print(min_value(game_tree))
#print(max_value(game_tree))

def max_action_value(game_tree):
    if type(game_tree) != list:
        return None, game_tree
    else:       
        value = -1*math.inf
        index = -1
        for i,t in enumerate(game_tree):
            min_val = min_value(t)
            if min_val > value:
                value = min_val
                index = i
        return index, value


                           
def min_action_value(game_tree):
    if type(game_tree) != list:
        return None, game_tree
    else:       
        value = math.inf
        index = -1
        for i,t in enumerate(game_tree):
            max_val = max_value(t)
            if max_val < value:
                value = max_val
                index = i
        return index, value

    
game_tree = [0, [-2, 1], 5]
    
action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

#game_tree = 3

#action, value = min_action_value(game_tree)
#print("Best action if playing min:", action)
#print("Best guaranteed utility:", value)
#print()
#action, value = max_action_value(game_tree)
#print("Best action if playing max:", action)
#print("Best guaranteed utility:", value)

#game_tree = [1, 2, [3]]

#action, value = min_action_value(game_tree)
#print("Best action if playing min:", action)
#print("Best guaranteed utility:", value)
#print()
#action, value = max_action_value(game_tree)
#print("Best action if playing max:", action)
#print("Best guaranteed utility:", value)

from math import inf

pruned_tree = [
    2, [-1], [1], 4
    ]
    

pruning_events = [
    (2, -1), (2, 1)
    ]

from math import inf

pruned_tree = [
    0, [-2, 1], 5
    ]
    

pruning_events = [
    (1, 0)
    ]

from math import inf

pruned_tree = [
    3, [[2], [4, [7, -2]]], 0
    ]
    

pruning_events = [
    (3, 2), (3, -2), (3, 0)
    ]