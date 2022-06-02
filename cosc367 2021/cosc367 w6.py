from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment
            
#from csp import *
##from student_answer import generate_and_test

#simple_csp = CSP(
    #var_domains={x: set(range(1, 5)) for x in 'abc'},
    #constraints={
        #lambda a, b: a < b,
        #lambda b, c: b < c,
        #})

#solutions = sorted(str(sorted(solution.items())) for solution 
                   #in generate_and_test(simple_csp))
#print("\n".join(solutions))

#crossword_puzzle = CSP(
    #var_domains={
        ## read across:
        #'a1': set("ant,big,bus,car".split(',')),
        #'a3': set("book,buys,hold,lane,year".split(',')),
        #'a4': set("ant,big,bus,car,has".split(',')),
        ## read down:
        #'d1': set("book,buys,hold,lane,year".split(',')),
        #'d2': set("ginger,search,symbol,syntax".split(',')),
        #},
    #constraints={
        #lambda a1, d1: a1[0] == d1[0],
        #lambda d1, a3: d1[2] == a3[0],
        #lambda a1, d2: a1[2] == d2[0],
        #lambda d2, a3: d2[2] == a3[2],
        #lambda d2, a4: d2[4] == a4[0],
        #})

#solution = next(iter(generate_and_test(crossword_puzzle)))

## printing the puzzle similar to the way it actually  looks 
#pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
    #solution['d1'], "", solution['d2'], fillvalue=" ")]
#pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
#print("\n".join(pretty_puzzle))

from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("bus has".split()),
        'a3': set("lane year".split()),
        'a4': set("ant car".split()),
        # read down:
        'd1': set("buys hold".split()),
        'd2': set("search syntax".split()),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })

#print(sorted(crossword_puzzle.var_domains['a1']))

from csp import CSP
canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })

import itertools, copy 
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

#simple_csp = CSP(
    #var_domains={x: set(range(1, 5)) for x in 'abc'},
    #constraints={
        #lambda a, b: a < b,
        #lambda b, c: b < c,
        #})

#csp = arc_consistent(simple_csp)
#for var in sorted(csp.var_domains.keys()):
    #print("{}: {}".format(var, sorted(csp.var_domains[var])))
    
#csp = CSP(var_domains={x:set(range(10)) for x in 'abc'},
              #constraints={lambda a,b,c: 2*a+b+2*c==10}) 
    
#csp = arc_consistent(csp)
#for var in sorted(csp.var_domains.keys()):
    #print("{}: {}".format(var, sorted(csp.var_domains[var])))    
    
csp = CSP(
    var_domains = {var:{0,1,2} for var in 'abcd'},
    constraints = {
       lambda a, b, c: a > b + c,
       lambda c, d: c > d
       }
    )

from csp import Relation

relations = [
    Relation(header=['a', 'b', 'c'],
             tuples={(1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 0, 1)}
        ### COMPLETE ###
    ),
    Relation(header=['c', 'd'],
             tuples={(1, 0), (2, 0), (2, 1)})
    ### COMPLETE ###
]

#print(len(relations))
#print(all(type(r) is Relation for r in relations))

csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'abcd'},
   constraints = {
      lambda a, b: a == abs(b),
      lambda c, d: c > d,
      lambda a, b, c: a * b > c + 1
      }
   )

from csp import Relation

relations = [
    Relation(header=['a', 'b'],
             tuples={(1,-1), (0, 0), (1, 1)}),
    
    Relation(header=['c', 'd'],
             tuples={(0,-1), (1, -1), (1, 0)}),
    
    Relation(header=['a', 'b', 'c'],
             tuples={(-1, -1, -1), (1, 1, -1)}),     
      ### COMPLETE ###
      ] 

relations_after_elimination = [
    Relation(header=['b', 'c'],
             tuples={(1, -1)}),    
    
    Relation(header=['c', 'd'],
             tuples={(0,-1), (1, -1), (1, 0)}),
    ### COMPLETE ###
    
    ] 

#print(len(relations))
#print(all(type(r) is Relation for r in relations))
#print(sorted(sorted(relations)[1].tuples))
#print(len(relations_after_elimination))
#print(all(type(r) is Relation for r in relations_after_elimination))
#print(sorted(relations_after_elimination)[0].header)

import itertools, copy 
from csp import scope, satisfies, CSP

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

    
def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment

domains = {x: set(range(0 if x != "f" else 1, 10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}, 'c3': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        #lambda t, w, o, f, u, r: len([t,w,o,f,u,r]) == len(set([t,w,o,f,u,r])),
        lambda o, r, c1    :      o + o == r + 10 * c1, # one of the constraints
        lambda w, c1, u, c2 : w + w + c1 == u + 10 * c2, # add more constraints
        lambda t, c2, o, c3  :t + t + c2 == o + 10 * c3,
        lambda f, c3: f == c3
        })

#print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
#print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour")) 

#new_csp = arc_consistent(cryptic_puzzle)
#print(sorted(new_csp.var_domains['r']))

#new_csp = arc_consistent(cryptic_puzzle)
#print(sorted(new_csp.var_domains['w']))

#from collections import OrderedDict
#new_csp = arc_consistent(cryptic_puzzle)
#solutions = []
#for solution in generate_and_test(new_csp):
    #solutions.append(sorted((x, v) for x, v in solution.items()
                            #if x in "twofur"))
#print(len(solutions))
#solutions.sort()
#print(solutions[0])
#print(solutions[5])

