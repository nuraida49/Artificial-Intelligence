from csp import CSP

csp_instance = CSP(
   var_domains = {
       'a': {1,2},
       'b': {1,2},
       'c': {3,4},
       'd': {1,2,3,4}},
   
   constraints = {
      lambda a, b: a >= b,
      lambda a, b: b >= a,
      lambda a, b, c: c > a + b,
      lambda d: d <= d,
   }
)

#from csp import CSP

#assert type(csp_instance) is CSP
#print(sorted(csp_instance.var_domains.keys()))
#print(len(csp_instance.constraints))
#print(sorted(csp_instance.var_domains['a']))


def select(population, error, max_error, r):
    fitness_list = []
    fitness = max_error - error
    for x in population:
        fitness_list.append(fitness(x))
    fitness_sum = sum(fitness_list)
    total = []
    running_total = 0
    for n in fitness_list:
        running_total += (n/fitness_sum)
        total.append(running_total)
    for i, individual in enumerate(population):
        if r < total[i]:
            return individual
              
            
population = ['a', 'b']
            
def error(x):
    return {'a': 14,
            'b': 12}[x]

max_error = 15

#for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
    #print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.



def num_parameters(unit_counts):
    if len(unit_counts) == 1:
        return 0
    elif len(unit_counts) == 2:
        return (unit_counts[0] * unit_counts[1]) + unit_counts[1]
    elif len(unit_counts) == 3:
        return (unit_counts[0] * unit_counts[1]) + (unit_counts[1] * unit_counts[-1]) + unit_counts[1] + unit_counts[-1]
    else:
        total = 0
        for i in range(len(unit_counts)-1):
            total += unit_counts[i] * unit_counts[i+1]
            total += unit_counts[i+1]
        return total
    
#print(num_parameters([2, 4, 2]))
#print(num_parameters([2, 4, 3, 4]))
#print(num_parameters([1]))

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
        
def num_crossovers(parent_expression1, parent_expression2):
    if type(parent_expression1) == list and type(parent_expression2) == list:
        depth_expr1 = depth(parent_expression1)
        depth_expr2 = depth(parent_expression2)
        if depth_expr1 == 1 and depth_expr2 == 1:
            return len(parent_expression1) * len(parent_expression2)
        elif depth_expr1 == 1 and depth_expr2 > 1:
            return len(parent_expression1) 
    elif (type(parent_expression1) == str or type(parent_expression1) == int) and type(parent_expression2) == list:
        return len(parent_expression2)
    elif (type(parent_expression2) == str or type(parent_expression2) == int) and type(parent_expression1) == list:
        return len(parent_expression1)


#expression1 = ['+', 12, 'x']
#expression2 = ['-', 3, 6]
#print(num_crossovers(expression1, expression2))
#expression1 = 'weight'
#expression2 = ['-', 8, 4]
#print(num_crossovers(expression1, expression2))