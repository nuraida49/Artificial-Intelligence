import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
def helper(knowledgebase, result):
    for implication in knowledgebase[1]:
        if implication not in result:
            return False
    return True
        
def forward_deduce(knowledgebase_str):
    knowledgebase_str = list(clauses(knowledgebase_str))
    result = []
    i = 0
    while i < len(knowledgebase_str):
        knowledgebase = knowledgebase_str[i]
        if helper(knowledgebase, result):
            result.append(knowledgebase_str.pop(i)[0])
            i = 0
        else:
            i += 1
    return result
    
#kb = """
#a :- b.
#b.
#"""

#print(", ".join(sorted(forward_deduce(kb))))

#kb = """
#good_programmer :- correct_code.
#correct_code :- good_programmer.
#"""

#print(", ".join(sorted(forward_deduce(kb))))

#kb = """
#a :- b, c.
#b :- d, e.
#b :- g, e.
#c :- e.
#d.
#e.
#f :- a,
     #g.
#"""

#print(", ".join(sorted(forward_deduce(kb))))

import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return self.query
        
    def is_goal(self, node):
        return len(node) == 0

    def outgoing_arcs(self, tail_node):
        tails = list(tail_node)
        for clause in self.clauses:
            if clause[0] == tails[0]:
                head = clause[1]
                yield Arc(tail_node, head, str(tail_node) + '->' + str(head), 0)

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first search."""
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

#from search import *

#kb = """
#a :- b, c.
#b :- d, e.
#b :- g, e.
#c :- e.
#d.
#e.
#f :- a,
     #g.
#"""

#query = {'a'}
#if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    #print("The query is true.")
#else:
    #print("The query is not provable.")
    
#from search import *

#kb = """
#a :- b, c.
#b :- d, e.
#b :- g, e.
#c :- e.
#d.
#e.
#f :- a,
     #g.
#"""

#query = {'a', 'b', 'd'}
#if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    #print("The query is true.")
#else:
    #print("The query is not provable.")
    
#kb = """
#all_tests_passed :- program_is_correct.
#all_tests_passed.
#"""

#query = {'program_is_correct'}
#if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    #print("The query is true.")
#else:
    #print("The query is not provable.")
    
#kb = """
#a :- b.
#"""

#query = {'c'}
#if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    #print("The query is true.")
#else:
    #print("The query is not provable.")