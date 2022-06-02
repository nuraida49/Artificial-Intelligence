from search import *
from math import sqrt
from heapq import *

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        temp_edges = set()
        for edge in edges:
            cost = self.distance(locations[edge[0]], locations[edge[1]])
            temp_edges.add((edge[0], edge[1], cost))
            temp_edges.add((edge[1], edge[0], cost))
        super(LocationGraph, self).__init__(nodes=nodes, edge_list=list(temp_edges), starting_nodes=starting_nodes,
                                            goal_nodes=goal_nodes, estimates=estimates)
        self.locations = locations

    def outgoing_arcs(self, node):
        arcs = ExplicitGraph.outgoing_arcs(self, node)
        return sorted(arcs, key=lambda arc: arc[2])

    def distance(self, point1, point2):
        xdist = point1[0] - point2[0]
        ydist = point1[1] - point2[1]
        return sqrt(xdist ** 2 + ydist ** 2)
            
#graph = LocationGraph(nodes=set('ABC'),
                      #locations={'A': (0, 0),
                                 #'B': (3, 0),
                                 #'C': (3, 4)},
                      #edges={('A', 'B'), ('B','C'),
                             #('C', 'A')},
                      #starting_nodes=['A'],
                      #goal_nodes={'C'})


#for arc in graph.outgoing_arcs('A'):
    #print(arc)

#for arc in graph.outgoing_arcs('B'):
    #print(arc)

#for arc in graph.outgoing_arcs('C'):
    #print(arc)
    
#pythagorean_graph = LocationGraph(
    #nodes=set("abc"),
    #locations={'a': (5, 6),
               #'b': (10,6),
               #'c': (10,18)},
    #edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    #starting_nodes=['a'],
    #goal_nodes={'c'})

#for arc in pythagorean_graph.outgoing_arcs('a'):
    #print(arc)    
    
from search import *
from math import sqrt
import heapq

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        temp_edges = set()
        for edge in edges:
            cost = self.distance(locations[edge[0]], locations[edge[1]])
            temp_edges.add((edge[0], edge[1], cost))
            temp_edges.add((edge[1], edge[0], cost))
        super(LocationGraph, self).__init__(nodes=nodes, edge_list=list(temp_edges), starting_nodes=starting_nodes,
                                            goal_nodes=goal_nodes, estimates=estimates)
        self.locations = locations

    def outgoing_arcs(self, node):
        arcs = ExplicitGraph.outgoing_arcs(self, node)
        return sorted(arcs, key=lambda arc: arc[2])

    def distance(self, point1, point2):
        xdist = point1[0] - point2[0]
        ydist = point1[1] - point2[1]
        return sqrt(xdist ** 2 + ydist ** 2)
      
class PriorityFrontier(Frontier):
    def __init__(self):
        self.container = []
        
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """
        self.container.append(path)
        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self
            
    def __next__(self):
        while self.container:
            result = heapq.nsmallest(1, self.container, key = lambda path : sum(arc.cost for arc in path))
            self.container.remove(result[-1])
            return result[-1]
            
        else:
            raise StopIteration   # don't change this one    
        
from search import *
graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A', 1), ('S','B',2),
               ('A', 'G', 3), ('B', 'G', 2)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'C', 'G'},
    edge_list=[('S','A', 1), ('S','C',2), ('S', 'B', 2),
               ('A', 'G', 3), ('C', 'G', 2), ('B', 'G', 2)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)
#from search import *
                
#graph = LocationGraph(nodes=set('ABC'),
                      #locations={'A': (0, 0),
                                 #'B': (3, 0),
                                 #'C': (3, 4)},
                      #edges={('A', 'B'), ('B','C'),
                             #('B', 'A'), ('C', 'A')},
                      #starting_nodes=['A'],
                      #goal_nodes={'C'})

#solution = next(generic_search(graph, LCFSFrontier()))
#print_actions(solution)

#from search import *
##from student_answer import LocationGraph, LCFSFrontier

#graph = LocationGraph(nodes=set('ABC'),
                      #locations={'A': (0, 0),
                                 #'B': (3, 0),
                                 #'C': (3, 4)},
                      #edges={('A', 'B'), ('B','C'),
                             #('B', 'A')},
                      #starting_nodes=['A'],
                      #goal_nodes={'C'})

#solution = next(generic_search(graph, LCFSFrontier()))
#print_actions(solution)

#from search import *
##from student_answer import LocationGraph, LCFSFrontier

#pythagorean_graph = LocationGraph(
    #nodes=set("abc"),
    #locations={'a': (5, 6),
               #'b': (10,6),
               #'c': (10,18)},
    #edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    #starting_nodes=['a'],
    #goal_nodes={'c'})

#solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
#print_actions(solution)

#from search import *
##from student_answer import LCFSFrontier

#graph = ExplicitGraph(nodes=set('ABCD'),
                      #edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                 #('B', 'C', 3), ('C', 'D', 1)],
                      #starting_nodes=['A'],
                      #goal_nodes={'D'})

#solution = next(generic_search(graph, LCFSFrontier()))
#print_actions(solution)

#from search import *
##from student_answer import LCFSFrontier

#graph = ExplicitGraph(nodes=set('ABCD'),
                      #edge_list=[('A', 'B', 2), ('A', 'D', 7),
                                 #('B', 'C', 3), ('C', 'D', 1)],
                      #starting_nodes=['A'],
                      #goal_nodes={'D'})

#solution = next(generic_search(graph, LCFSFrontier()))
#print_actions(solution)

