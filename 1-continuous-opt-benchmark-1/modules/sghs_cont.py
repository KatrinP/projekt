#! usr/bin/env python3

# Original GHS algorithm
import csv
from random import random
from numpy.random import randint
import os

def check_io(total):
    base = os.path.basename(__file__)
    filename = os.path.splitext(base)[0]
    if not os.path.exists(os.path.join(os.getcwd(), 'data', filename)):
        os.mkdir(os.path.join(os.getcwd(), 'data', filename))
    path0 = os.path.join(os.getcwd(), 'data', filename, 'fitness')
    if not os.path.exists(path0):
        os.mkdir(path0)
    path = os.path.join(path0, str(total))
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def objective_function(vector, problem_size):
    sum = 0
    for val in vector:
        sum += val ** 2
    return sum

def rand_in_bounds(minimum, maximum):
    return minimum + ((maximum - minimum) * random())

def random_vector(search_space):
    i = 0
    limit = len(search_space)
    random_vector = [0 for i in range(limit)]
    
    for i in range(limit):
        random_vector[i] = rand_in_bounds(search_space[i][0], search_space[i][1])   
    return random_vector

def create_random_harmony(search_space, problem_size):
    harmony = {}
    harmony["vector"] = random_vector(search_space)
    harmony["fitness"] = objective_function(harmony["vector"], problem_size)
    return harmony

def initialize_harmony_memory(search_space, HMS, problem_size, factor=3):
    memory = [create_random_harmony(search_space, problem_size) for i in range(HMS*factor)]
    #memory = sorted(memory, key=itemgetter('fitness')) 
    memory = sorted(memory, key= lambda k: k["fitness"])
    return [memory[i] for i in range(HMS)]

def create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, max_iter, gn):
    limit = len(search_space)
    vector = [0 for i in range(limit)]

    PAR = PARmin + ((PARmax - PARmin)/max_iter)*gn

    for i in range(limit):
        if random() < HMCR:
            value = memory[randint(0, len(memory)-1)]["vector"][i] + rand_in_bounds(-1.0, 1.0)
            if random() < PAR:
                value = best["vector"][i] # the same current pitch
            if value < search_space[i][0]:
                value = search_space[i][0]
            if value > search_space[i][1]:
                value = search_space[i][1]

            vector[i] = value
        else:
            vector[i] = rand_in_bounds(search_space[i][0], search_space[i][1])
    
    return {"vector": vector}

def search(search_space, max_iter, HMS, HMCR, PARmin, PARmax, problem_size, total):
    path = check_io(total)
    with open(os.path.join(path, 'fitness.csv'), 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        memory = initialize_harmony_memory(search_space, HMS, problem_size)
        best = memory[0]
        for i in range(max_iter):
            harm = create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, max_iter, i)
            harm["fitness"] = objective_function(harm["vector"], problem_size)
            if harm["fitness"] < best["fitness"]:
                best = harm
            memory.append(harm)
            memory = sorted(memory, key= lambda k: k["fitness"])
            del memory[-1]

            # write fitness
            spamwriter.writerow([i,best['fitness']])

    return best
