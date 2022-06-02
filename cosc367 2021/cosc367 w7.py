import itertools
def n_queens_neighbours(state):
    n_queens_neighbours = []
    for i in  range(len(state)):
        for j in  range(len(state)):
            if i != j:
                temp_list = list(state)
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
                if tuple(temp_list) not in n_queens_neighbours:
                    n_queens_neighbours.append(tuple(temp_list))
    return sorted(n_queens_neighbours)

#print(neighbours((1, 2)))
#print(neighbours((1, 3, 2)))
#print(neighbours((1, 2, 3)))
#print(neighbours((1,)))
#for neighbour in neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
    #print(neighbour)
#for neighbour in neighbours((2, 3, 1, 4)):
    #print(neighbour)
    
def n_queens_cost(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            x, y = j - i,  state[j] - state[i]
            if x == 0 or y == 0: continue

            r = abs(x / y)
            if r == 1:
                conflicts += 1

    return conflicts

#print(n_queens_cost((1, 2)))
#print(n_queens_cost((1, 3, 2)))
#print(n_queens_cost((1, 2, 3)))
#print(n_queens_cost((1,)))
#print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
#print(n_queens_cost((2, 3, 1, 4)))


def greedy_descent(initial_state, neighbours, cost):
    state = [initial_state]
    current_state = initial_state
    min_cost = False   
    while not min_cost:
        neighbour_list = neighbours(current_state)
        if len(neighbour_list) == 0:
            break      
        cost_list = []       
        for neighbour in neighbour_list:
            cost_list.append(cost(neighbour))
        if min(cost_list) < cost(current_state):
            min_index = cost_list.index(min(cost_list))
            current_state = neighbour_list[min_index]
            state.append(current_state)
        else:
            min_cost = True      
    return state
        
#def cost(x):
    #return x**2

#def neighbours(x):
    #return [x - 1, x + 1]

#for state in greedy_descent(4, neighbours, cost):
    #print(state)
    
#def cost(x):
    #return x**2

#def neighbours(x):
    #return [x - 1, x + 1]

#for state in greedy_descent(-6.75, neighbours, cost):
    #print(state)

from itertools import combinations
    
def n_queens_neighbours(state):
    n_queens_neighbours = []
    for i in  range(len(state)):
        for j in  range(len(state)):
            if i != j:
                temp_list = list(state)
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
                if tuple(temp_list) not in n_queens_neighbours:
                    n_queens_neighbours.append(tuple(temp_list))
    return sorted(n_queens_neighbours)


def n_queens_cost(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            x, y = j - i,  state[j] - state[i]
            if x == 0 or y == 0: continue

            r = abs(x / y)
            if r == 1:
                conflicts += 1

    return conflicts


def greedy_descent(initial_state, neighbours, cost):
    state = [initial_state]
    current_state = initial_state
    min_cost = False   
    while not min_cost:
        neighbour_list = neighbours(current_state)
        if len(neighbour_list) == 0:
            break      
        cost_list = []       
        for neighbour in neighbour_list:
            cost_list.append(cost(neighbour))
        if min(cost_list) < cost(current_state):
            min_index = cost_list.index(min(cost_list))
            current_state = neighbour_list[min_index]
            state.append(current_state)
        else:
            min_cost = True      
    return state


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    current_state = random_state()
    optimal_state = False
    while not optimal_state:
        states = greedy_descent(current_state, neighbours, cost)
        for state in states:
            print(state)
        if cost(states[-1]) > 0:
            print("RESTART")
            current_state = random_state()
        else:
            optimal_state = True
            
#import random
#neighbours, cost = n_queens_neighbours, n_queens_cost

#N = 6
#random.seed(0)

#def random_state():
    #return tuple(random.sample(range(1,N+1), N))   

#greedy_descent_with_random_restart(random_state, neighbours, cost)    

#import random

#N = 8
#random.seed(0)

#def random_state():
    #return tuple(random.sample(range(1,N+1), N))   

#greedy_descent_with_random_restart(random_state, neighbours, cost)
    
def roulette_wheel_select(population, fitness, r):
    fitness_list = []
    
    for x in population:
        fitness_list.append(fitness(x))
        
    fitness_sum = sum(fitness_list)
    total = []
    running_total = 0
    
    for n in fitness_list:
        running_total += (n/fitness_sum)
        total.append(running_total)
    
    for i, individual  in enumerate(population):
        if r < total[i]:
            return individual    
        
population = ['a', 'b']
        
def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))
    
population = [0, 1, 2]
    
def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))