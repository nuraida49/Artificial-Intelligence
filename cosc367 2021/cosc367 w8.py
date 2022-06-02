def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will enentually hold the value we are interested in
    for var in assignment:
        value = network[var]
        parents = []
        for item in value['Parents']:
            parents.append(assignment[item])
        parents = tuple(parents)
        p *= value['CPT'][parents] if assignment[var] else 1 - value['CPT'][parents]
        # Extract the probability of var=true from the network
        # by finding the right assignment for Parents and getting the
        # corresponding CPT. 
        
        # Update p by multiplying it by probablity var=true or var=false
        # depending on how var appears in the given assignment.
    
    return p
        
#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.2
            #}},
#}

#p = joint_prob(network, {'A': True})
#print("{:.5f}".format(p))

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.2
            #}},
#}

#p = joint_prob(network, {'A': False})
#print("{:.5f}".format(p))

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.1
            #}},
            
    #'B': {
        #'Parents': ['A'],
        #'CPT': {
            #(True,): 0.8,
            #(False,): 0.7,
            #}},
    #}
 
#p = joint_prob(network, {'A': False, 'B':True})
#print("{:.5f}".format(p)) 

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.1
            #}},
            
    #'B': {
        #'Parents': ['A'],
        #'CPT': {
            #(True,): 0.8,
            #(False,): 0.7,
            #}},
    #}
 
#p = joint_prob(network, {'A': False, 'B':False})
#print("{:.5f}".format(p)) 

#network = {
    #'Burglary': {
        #'Parents': [],
        #'CPT': {
            #(): 0.001
            #}},
            
    #'Earthquake': {
        #'Parents': [],
        #'CPT': {
            #(): 0.002,
            #}},
    #'Alarm': {
        #'Parents': ['Burglary','Earthquake'],
        #'CPT': {
            #(True,True): 0.95,
            #(True,False): 0.94,
            #(False,True): 0.29,
            #(False,False): 0.001,
            #}},

    #'John': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.9,
            #(False,): 0.05,
            #}},

    #'Mary': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.7,
            #(False,): 0.01,
            #}},
    #}

#p = joint_prob(network, {'John': True, 'Mary': True,
                         #'Alarm': True, 'Burglary': False,
                         #'Earthquake': False})
#print("{:.8f}".format(p))
import itertools
def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    # Find the hidden variables
    # Initialise a raw distribution to [0, 0]
    false_var, true_var = 0, 0
    assignment = dict(evidence) # create a partial assignment
    for values in itertools.product((True, False), repeat=len(hidden_vars)):
        hidden_assignments = {var:val for var,val in zip(hidden_vars, values)} 
                # Update the assignment to include the query variable
        hidden_assignments.update(evidence)
        hidden_assignments.update({query_var: True})
        # Update the assignment (we now have a complete assignment)
        # Update the raw distribution by the probability of the assignment.        
        true_var += joint_prob(network, hidden_assignments)
        hidden_assignments[query_var] = False
        false_var += joint_prob(network, hidden_assignments)
            # Normalise the raw distribution and return it
    normalization = true_var + false_var
    result = {True: true_var / normalization, False: false_var / normalization}
    return result

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.2
            #}},
#}

#answer = query(network, 'A', {})
#print("P(A=true) = {:.5f}".format(answer[True]))
#print("P(A=false) = {:.5f}".format(answer[False]))
        

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.1
            #}},
            
    #'B': {
        #'Parents': ['A'],
        #'CPT': {
            #(True,): 0.8,
            #(False,): 0.7,
            #}},
    #}
 
#answer = query(network, 'B', {'A': False})
#print("P(B=true|A=false) = {:.5f}".format(answer[True]))
#print("P(B=false|A=false) = {:.5f}".format(answer[False]))

#network = {
    #'A': {
        #'Parents': [],
        #'CPT': {
            #(): 0.1
            #}},
            
    #'B': {
        #'Parents': ['A'],
        #'CPT': {
            #(True,): 0.8,
            #(False,): 0.7,
            #}},
    #}
 
#answer = query(network, 'B', {})
#print("P(B=true) = {:.5f}".format(answer[True]))
#print("P(B=false) = {:.5f}".format(answer[False]))

#network = {
    #'Burglary': {
        #'Parents': [],
        #'CPT': {
            #(): 0.001
            #}},
            
    #'Earthquake': {
        #'Parents': [],
        #'CPT': {
            #(): 0.002,
            #}},
    #'Alarm': {
        #'Parents': ['Burglary','Earthquake'],
        #'CPT': {
            #(True,True): 0.95,
            #(True,False): 0.94,
            #(False,True): 0.29,
            #(False,False): 0.001,
            #}},

    #'John': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.9,
            #(False,): 0.05,
            #}},

    #'Mary': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.7,
            #(False,): 0.01,
            #}},
    #}

#answer = query(network, 'Burglary', {'John': True, 'Mary': True})
#print("Probability of a burglary when both\n"
      #"John and Mary have called: {:.3f}".format(answer[True])) 

#network = {
    #'Burglary': {
        #'Parents': [],
        #'CPT': {
            #(): 0.001
            #}},
            
    #'Earthquake': {
        #'Parents': [],
        #'CPT': {
            #(): 0.002,
            #}},
    #'Alarm': {
        #'Parents': ['Burglary','Earthquake'],
        #'CPT': {
            #(True,True): 0.95,
            #(True,False): 0.94,
            #(False,True): 0.29,
            #(False,False): 0.001,
            #}},

    #'John': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.9,
            #(False,): 0.05,
            #}},

    #'Mary': {
        #'Parents': ['Alarm'],
        #'CPT': {
            #(True,): 0.7,
            #(False,): 0.01,
            #}},
    #}

#answer = query(network, 'John', {'Mary': True})
#print("Probability of John calling if\n"
      #"Mary has called: {:.5f}".format(answer[True])) 
      
network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 1/100000
            }},
            
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 1/100,
            }},
    }

#answer = query(network, 'Disease', {'Test': True})
#print("The probability of having the disease\n"
      #"if the test comes back positive: {:.8f}"
      #.format(answer[True]))

#answer = query(network, 'Disease', {'Test': False})
#print("The probability of having the disease\n"
      #"if the test comes back negative: {:.8f}"
      #.format(answer[True]))
      
network = {
    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1,
            }},
            
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},
    
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 1/100
            }},    
    }

#answer = query(network, 'Virus', {'A': True})
#print("The probability of carrying the virus\n"
      #"if test A is positive: {:.5f}"
      #.format(answer[True]))

#answer = query(network, 'Virus', {'B': True})
#print("The probability of carrying the virus\n"
      #"if test B is positive: {:.5f}"
      #.format(answer[True]))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2 # You can change this value
            }
        
    },
    
    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.3,
            (False,): 0.4, # You can change this value
            }
        
    },
    
    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.2,
            (False,): 0.3 # You can change this value
            }
        
    },    
    
# add more variables

}

#print(sorted(network.keys()))
#bd_dependence = network['D']['CPT'][(False,)] != network['D']['CPT'][(True,)]
#be_dependence = network['E']['CPT'][(False,)] != network['E']['CPT'][(True,)]
#print(bd_dependence and be_dependence)