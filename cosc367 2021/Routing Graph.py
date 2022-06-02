import math
from search import *
from heapq import *

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map_str = map_str
        self.map_graph = []
        self.startings_list = []
        self.goal_nodes = []
        
        self.graph_map(self.map_str)
        
    def graph_map(self, map_str):
        """Converts map string to (row, column) format."""
        real_map = (map_str.strip()).split('\n')
        for item in real_map:
            self.map_graph.append(list(item.strip()))
        for i in range(len(self.map_graph)):
            for j in range(len(self.map_graph[i])):
                row_, column_ = i, j
                if self.map_graph[row_][column_] == "S":
                    self.startings_list.append((row_, column_, math.inf))
                elif self.map_graph[row_][column_].isdigit():
                    self.startings_list.append((row_, column_, int(self.map_graph[row_][column_])))
                elif self.map_graph[row_][column_] == "G":
                    self.goal_nodes.append((row_, column_))
        
    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.

        """
        for start_node in self.startings_list:
            yield start_node

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        return (node[0], node[1]) in self.goal_nodes

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        directions = [('N' , -1, 0),
                      ('E' ,  0, 1),
                      ('S' ,  1, 0),
                      ('W' ,  0, -1),]
        borders = ['X', '+', '-', '|']
        possible_moves = []
        for direction in directions:
            rows = tail_node[0] + direction[1]
            columns = tail_node[1] + direction[2]            
            if self.map_graph[rows][columns] not in borders and tail_node[2] > 0:
                state = (rows, columns, tail_node[2] - 1)
                yield Arc(tail_node, state, direction[0], 5)                
        if self.map_graph[tail_node[0]][tail_node[1]] == "F" and tail_node[2] < 9:
            rows, columns = tail_node[0], tail_node[1]
            state = (rows, columns, 9)
            yield Arc(tail_node, state, 'Fuel up', 15)
        
    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""

        return min([(abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 5 for goal in self.goal_nodes])

        
#import math
    
#map_str = """\
#+-------+
#|  9  XG|
#|X XXX  |
#| S  0FG|
#+-------+
#"""

#graph = RoutingGraph(map_str)

#print("Starting nodes:", sorted(graph.starting_nodes()))
#print("Outgoing arcs (available actions) at starting states:")
#for s in sorted(graph.starting_nodes()):
    #print(s)
    #for arc in graph.outgoing_arcs(s):
        #print ("  " + str(arc))

#node = (1,1,5)
#print("\nIs {} goal?".format(node), graph.is_goal(node))
#print("Outgoing arcs (available actions) at {}:".format(node))
#for arc in graph.outgoing_arcs(node):
    #print ("  " + str(arc))

#node = (1,7,2)
#print("\nIs {} goal?".format(node), graph.is_goal(node))
#print("Outgoing arcs (available actions) at {}:".format(node))
#for arc in graph.outgoing_arcs(node):
    #print ("  " + str(arc))

#node = (3, 7, 0)
#print("\nIs {} goal?".format(node), graph.is_goal(node))

#node = (3, 7, math.inf)
#print("\nIs {} goal?".format(node), graph.is_goal(node))

#node = (3,6,5)
#print("\nIs {} goal?".format(node), graph.is_goal(node))
#print("Outgoing arcs (available actions) at {}:".format(node))
#for arc in graph.outgoing_arcs(node):
    #print ("  " + str(arc))

#node = (3,6,9)
#print("\nIs {} goal?".format(node), graph.is_goal(node))
#print("Outgoing arcs (available actions) at {}:".format(node))
#for arc in graph.outgoing_arcs(node):
    #print ("  " + str(arc))

##test 2
    
#map_str = """\
#+--+
#|GS|
#+--+
#"""

#graph = RoutingGraph(map_str)

#print("Starting nodes:", sorted(graph.starting_nodes()))
#print("Outgoing arcs (available actions) at the start:")
#for start in graph.starting_nodes():
    #for arc in graph.outgoing_arcs(start):
        #print ("  " + str(arc))



#node = (1,1,1)
#print("\nIs {} goal?".format(node), graph.is_goal(node))
#print("Outgoing arcs (available actions) at {}:".format(node))
#for arc in graph.outgoing_arcs(node):
    #print ("  " + str(arc))
    
##test 3
    
#map_str = """\
#+------+
#|S    S|
#|  GXXX|
#|S     |
#+------+
#"""

#graph = RoutingGraph(map_str)
#print("Starting nodes:", sorted(graph.starting_nodes()))

class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        """Initialised AStarFrontier objects with an instance of a graph"""
        self.map_graph = map_graph
        self.open_list = []
        self.close_list = set()
        self.counter = 1
        
        
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """
        if path[-1].head not in self.close_list:
            child_cost = sum([child.cost for child in path])
            heappush(self.open_list, (self.map_graph.estimated_cost_to_goal(path[-1].head) + child_cost, self.counter, path))
            self.counter += 1

    
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.

        """
        while self.open_list:
            path = heappop(self.open_list)[2]
            if path[-1].head not in self.close_list:
                self.close_list.add(path[-1].head)
                return path
        raise StopIteration
    
        
#from search import *
                
#map_str = """\
#+-------+
#|   G   |
#|       |
#|   S   |
#+-------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+-------+
#|  GG   |
#|S    G |
#|  S    |
#+-------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+-------+
#|     XG|
#|X XXX  |
#| S     |
#+-------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+-------+
#|  F  X |
#|X XXXXG|
#| 3     |
#+-------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+--+
#|GS|
#+--+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+---+
#|GF2|
#+---+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+----+
#| S  |
#| SX |
#|GX G|
#+----+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+---------+
#|         |
#|    G    |
#|         |
#+---------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)

#from search import *

#map_str = """\
#+----------------+
#|2              F|
#|XX     G 123    |
#|3XXXXXXXXXXXXXX |
#|  F             |
#|          F     |
#+----------------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_actions(solution)


def print_map(map_graph, frontier, solution):
    for i in range(len(map_graph.map_graph)):
        for j in range(len(map_graph.map_graph[i])):
            agent = True if map_graph.map_graph[i][j] in ['S', 'G'] else False
            node = (i, j, math.inf)                
            if solution != None and node in [child.tail for child in solution] and not agent: 
                print('*', end='')
            elif node in frontier.close_list and not agent: 
                print('.', end='')
            else: 
                print(map_graph.map_graph[i][j], end='')
        print()
        

#from search import *
        
#map_str = """\
#+----------------+
#|                |
#|                |
#|                |
#|                |
#|                |
#|                |
#|        S       |
#|                |
#|                |
#|     G          |
#|                |
#|                |
#|                |
#+----------------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+----------------+
#|                |
#|                |
#|                |
#|                |
#|                |
#|                |
#|        S       |
#|                |
#|                |
#|     G          |
#|                |
#|                |
#|                |
#+----------------+
#"""


#map_graph = RoutingGraph(map_str)
## changing the heuristic so the search behaves like LCFS
#map_graph.estimated_cost_to_goal = lambda node: 0

#frontier = AStarFrontier(map_graph)

#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+-------------+
#| G         G |
#|      S      |
#| G         G |
#+-------------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+-------+
#|     XG|
#|X XXX  |
#|  S    |
#+-------+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+--+
#|GS|
#+--+
#"""
#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+----+
#|    |
#| SX |
#| X G|
#+----+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+---------------+
#|    G          |
#|XXXXXXXXXXXX   |
#|           X   |
#|  XXXXXX   X   |
#|  X S  X   X   |
#|  X        X   |
#|  XXXXXXXXXX   |
#|               |
#+---------------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

#from search import *

#map_str = """\
#+---------+
#|         |
#|    G    |
#|         |
#+---------+
#"""

#map_graph = RoutingGraph(map_str)
#frontier = AStarFrontier(map_graph)
#solution = next(generic_search(map_graph, frontier), None)
#print_map(map_graph, frontier, solution)

def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int or object in leaf_symbols:
        return True
    elif type(object) == list:
        if len(object) == 3 and object[0] in function_symbols and is_valid_expression(object[1], function_symbols, leaf_symbols) is True and is_valid_expression(object[2], function_symbols, leaf_symbols) is True:
            return True
        return False
    return False

    
#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = 1

#print(is_valid_expression(expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = 'y'

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = 2.0

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['f', 123, 'x']

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['+', ['f', 1, 'x'], -1]

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y', -1, 0, 1]
#expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = 'f'

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))
        
#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['f', 1, 0, -1]

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['x', 0, 1]

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))

#function_symbolsfunction_symbols = ['f', '+']
#leaf_symbols = ['x', 'y']
#expression = ['g', 0, 'y']

#print(is_valid_expression(
        #expression, function_symbols, leaf_symbols))
        
def depth(expression):
    if type(expression) == int or type(expression) == str:
        return 0
    else:
        second_val = 1 + depth(expression[1])
        third_val = 1 + depth(expression[2])
        if second_val >= third_val:
            return second_val
        else:
            return third_val

#expression = 12
#print(depth(expression))

#expression = 'weight'
#print(depth(expression))

#expression = ['add', 12, 'x']
#print(depth(expression))

#expression = ['add', ['add', 22, 'y'], 'x']
#print(depth(expression))

#expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
#print(depth(expression))

def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    if type(expression) == str:
        return bindings[expression]
    else:
        value = bindings[expression[0]]
        second_val = evaluate(expression[1], bindings)
        third_val = evaluate(expression[2], bindings)
        return value(second_val, third_val)
    
#bindings = {}
#expression = 12
#print(evaluate(expression, bindings))
        
#bindings = {'x':5, 'y':10, 'time':15}
#expression = 'y'
#print(evaluate(expression, bindings))

#bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
#expression = ['add', 12, 'x']
#print(evaluate(expression, bindings))

#import operator

#bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
#expression = ['add', ['add', 22, 'y'], 'x']
#print(evaluate(expression, bindings))

import random

def coin():    
    return (10 * random.randint(0, 1)) > 5

def random_expression(function_symbols, leaves, max_depth):
    if not max_depth or coin():
        return leaves[random.randint(0, len(leaves) - 1)]
    else:
        return [function_symbols[random.randint(0, len(function_symbols) - 1)],             random_expression(function_symbols, leaves, max_depth - 1),
            random_expression(function_symbols, leaves, max_depth - 1)]                
                
#function_symbols = ['f', 'g', 'h']
#constant_leaves =  list(range(-2, 3))
#variable_leaves = ['x', 'y', 'i']
#leaves = constant_leaves + variable_leaves
#max_depth = 4

#for _ in range(10000):
    #expression = random_expression(function_symbols, leaves, max_depth)
    #if not is_valid_expression(expression, function_symbols, leaves):
        #print("The following expression is not valid:\n", expression)
        #break
#else:
    #print("OK")
    
#function_symbols = ['f', 'g', 'h']
#leaves = ['x', 'y', 'i'] + list(range(-2, 3))
#max_depth = 4

#expressions = [random_expression(function_symbols, leaves, max_depth)
               #for _ in range(10000)]

## Out of 10000 expressions, at least 1000 must be distinct
#_check_distinctness(expressions)

#function_symbols = ['f', 'g', 'h']
#leaves = ['x', 'y', 'i'] + list(range(-2, 3))
#max_depth = 4

#expressions = [random_expression(function_symbols, leaves, max_depth)
               #for _ in range(10000)]

## Out of 10000 expressions, there must be at least 100 expressions
## of depth 0, 100 of depth 1, ..., and 100 of depth 4.

#_check_diversity(expressions, max_depth)
    
def generate_rest(initial_sequence, expression, length):
    result = list(initial_sequence)
    count = 0
    while count < length:
        i = len(initial_sequence) + count
        x = result[i-2]
        y = result[i-1]
        bindings = {'x': x, '+': lambda x, y: x + y,
                    'y': y, '-': lambda x, y: x - y,
                    'i': i, '*': lambda x, y: x * y}
        result.append(evaluate(expression, bindings))
        count += 1
    return result[len(initial_sequence):]

#initial_sequence = [0, 1, 2]
#expression = 'i' 
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression,
                    #length_to_generate))

## no particular pattern, just an example expression
#initial_sequence = [-1, 1, 367]
#expression = 'i' 
#length_to_generate = 4
#print(generate_rest(initial_sequence,
                    #expression,
                    #length_to_generate))

#initial_sequence = [4, 6, 8, 10]
#expression = ['*', ['+', 'i', 2], 2]
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))

#initial_sequence = [4, 6, 8, 10]
#expression = ['+', 2, 'y']
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))
                    
#initial_sequence = [0, 1]
#expression = 'x'
#length_to_generate = 6
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))

## Fibonacci sequence
#initial_sequence = [0, 1]
#expression = ['+', 'x', 'y']
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))

#initial_sequence = [367, 367, 367]
#expression = 'y'
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))

## no pattern, just a demo
#initial_sequence = [0, 1, 2]
#expression = -1 
#length_to_generate = 5
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))

#initial_sequence = [0, 1, 2]
#expression = 'i'
#length_to_generate = 0
#print(generate_rest(initial_sequence, 
                    #expression, 
                    #length_to_generate))
#import random                    
#def predict_rest(sequence):
    #function_symbols = ['+', '-', '*']
    #leaves = ['x', 'y', 'i'] + list(range(-2,2))
    #max_depth = 3
    #found = False
    #count = 0
    #while not found:
        #expression = random_expression(function_symbols, leaves, max_depth)
        #initial_sequence = sequence[:2]
        #while count < len(sequence):
            #i = count + 2
            #x, y = sequence[i-2], sequence[i-1]
            #bindings = {'x': x, '+': lambda x, y: x + y,
                        #'y': y, '-': lambda x, y: x - y,
                        #'i': i, '*': lambda x, y: x * y}   
            #initial_sequence.append(evaluate(expression, bindings))
            #count += 1
        #total = 0
        #for instance in range(len(sequence)):
            #total += abs(sequence[instance] - initial_sequence[instance])
        #if total == 0:
            #found == True
    #return generate_rest(sequence, expression, 5)

def predict_rest(sequence):
    function_symbols = ['+', '-', '*']
    leaves = ['x', 'y', 'i'] + list(range(-2,2))
    max_depth = 3
    initial_sequence = sequence[:3]
    end_sequence = sequence[3:]
    for i in range(100000):
        expression = random_expression(function_symbols, leaves, max_depth)
        others = generate_rest(initial_sequence, expression, len(end_sequence))
        if others == end_sequence:
            break
        
    return generate_rest(sequence, expression, 5)

sequence = [0, 1, 2, 3, 4, 5, 6, 7]
the_rest = predict_rest(sequence)
print(sequence)
print(the_rest)

sequence = [0, 2, 4, 6, 8, 10, 12, 14]
print(predict_rest(sequence))

sequence = [31, 29, 27, 25, 23, 21]
print(predict_rest(sequence))

sequence = [0, 1, 4, 9, 16, 25, 36, 49]
print(predict_rest(sequence))

sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))

sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
print(predict_rest(sequence))

sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print(predict_rest(sequence))

sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print(predict_rest(sequence))