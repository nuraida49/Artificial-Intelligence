from search import *

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop() # FIX THIS return something instead
        else:
            raise StopIteration   # don't change this one

def main():
    # Example 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    # Example 2
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)


#if __name__ == "__main__":
    #main()
    
from search import *    
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0) # FIX THIS return something instead
        else:
            raise StopIteration   # don't change this one
        
#from search import *
##from student_answer import BFSFrontier

#graph = ExplicitGraph(nodes=set('SAG'),
                      #edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                      #starting_nodes = ['S'],
                      #goal_nodes = {'G'})

#solutions = generic_search(graph, BFSFrontier())
#solution = next(solutions, None)
#print_actions(solution)

#from search import *
##from student_answer import BFSFrontier

#flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                               #'Wellington', 'Gold Coast'],
                        #edge_list = [('Christchurch', 'Gold Coast'),
                                 #('Christchurch','Auckland'),
                                 #('Christchurch','Wellington'),
                                 #('Wellington', 'Gold Coast'),
                                 #('Wellington', 'Auckland'),
                                 #('Auckland', 'Gold Coast')],
                        #starting_nodes = ['Christchurch'],
                        #goal_nodes = {'Gold Coast'})

#my_itinerary = next(generic_search(flights, BFSFrontier()), None)
#print_actions(my_itinerary)

from search import *

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
        
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0) # FIX THIS return something instead
        else:
            raise StopIteration   # don't change this one
        
#graph = FunkyNumericGraph(4)
#for node in graph.starting_nodes():
    #print(node)
    
#graph = FunkyNumericGraph(4)
#for arc in graph.outgoing_arcs(7):
    #print(arc)

#graph = FunkyNumericGraph(3)
#solutions = generic_search(graph, BFSFrontier())
#print_actions(next(solutions))
#print()
#print_actions(next(solutions))

#from itertools import dropwhile

#graph = FunkyNumericGraph(3)
#solutions = generic_search(graph, BFSFrontier())
#print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))

from search import *
import copy

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        i, j = next((i, j) for i in range(n) for j in range(n)
                    if state[i][j] == BLANK) # find the blank tile
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes right
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        n = len(state)
        counter = 0
        test_list = []        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    if state[i][j] == BLANK:
                        test_list.append('True')                        
                else:
                    if state[i][j] == counter:
                        test_list.append('True') 
                    else:
                        test_list.append('False')
                counter += 1        
        if 'False' not in test_list:
            return True
        else:
            return False

        

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0) # FIX THIS return something instead
        else:
            raise StopIteration   # don't change this one
        
#from student_answer import SlidingPuzzleGraph, BFSFrontier
from search import generic_search, print_actions

graph = SlidingPuzzleGraph([[1, 2, 5],
                            [3, 4, 8],
                            [6, 7, ' ']])

solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))

#from student_answer import SlidingPuzzleGraph, BFSFrontier
from search import generic_search, print_actions

graph = SlidingPuzzleGraph([[3,' '],
                            [1, 2]])

solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))

from search import generic_search, print_actions

graph = SlidingPuzzleGraph([[1, ' ', 2],
                            [6,  4,  3],
                            [7,  8,  5]])

solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))