#! usr/bin/env python3

import random
import math
import os, sys
import time
import csv
import shutil

from ecl_to_alg import get_fitness


def objective_function(vector):
    result = get_fitness(vector)
    # result = random.choice([2000.13, 500.4, 5546.1, 1836.5, 222, 
        # 1000, 1500, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
    return result

def rand_in_bounds(minimum, maximum):
    return random.randint(minimum, maximum)

def random_vector():
    rand_vector = [random.randint(1, 25), random.randint(1, 25)]
    banned_list = [[1,1], [25,25], [1,25], [25,1]]
    
    if rand_vector not in banned_list:
        return rand_vector
    else:
        return random_vector()

def create_random_harmony():
    harmony = {}
    harmony["vector"] = random_vector()
    harmony["fitness"] = objective_function(harmony["vector"])
    return harmony

def initialize_harmony_memory(HMS):
    memory = [create_random_harmony() 
              for i in range(HMS)]
    #memory = sorted(memory, key=itemgetter('fitness')) 
    memory = sorted(memory, key= lambda k: k["fitness"])
    return [memory[i] for i in range(HMS)]

def create_harmony(search_space, memory, HMCR, PAR, bw):
    limit = len(search_space)
    vector = [0 for i in range(limit)]

    for i in range(limit):
        if random.random() < HMCR:
            value = memory[random.randint(0, len(memory)-1)]["vector"][i]
            if random.random() < PAR:
                value = value + rand_in_bounds(-1.0, 1.0)
            if value < search_space[0][0]:
                value = search_space[0][0]
            if value > search_space[0][1]:
                value = search_space[0][1]

            vector[i] = value
        else:
            vector = random_vector()
    
    return {"vector": vector}

def search(search_space, max_iter, HMS, HMCR, PAR, bw, total):
    memory = initialize_harmony_memory(HMS)
    best = memory[0]
    for i in range(max_iter):
        harm = create_harmony(search_space, memory, HMCR, PAR, bw)
        harm["fitness"] = objective_function(harm["vector"])
        if harm["fitness"] > best["fitness"]:
            best = harm
        memory.append(harm)
        memory = sorted(memory, key= lambda k: k["fitness"])

        del memory[0]

        # write fitness
        path0 = os.path.join(os.getcwd(), 'data', 'hs_2D_wp', 'fitness')
        if not os.path.exists(path0):
            os.mkdir(path0)
        path = os.path.join(path0, str(total))
        if not os.path.exists(path):
            os.mkdir(path)
        with open(os.path.join(path, 'fitness.csv'), 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([i,best['fitness']])

        ## write coordinates
        path20 = os.path.join(os.getcwd(), 'data', 'hs_2D_wp', 'vectors')
        if not os.path.exists(path20):
            os.mkdir(path20)
        path2 = os.path.join(path20, str(total))
        if not os.path.exists(path2):
            os.mkdir(path2)
        with open(os.path.join(path2, 'vector.csv'), 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([i,best['fitness'],best['vector']])

    return best


if __name__ == "__main__":
    # clean directories/files 
    if os.path.exists('results/hs_2D_wp_plot_runtime.txt'):
        os.remove('results/hs_2D_wp_plot_runtime.txt')

    path='data/hs_2D_wp/'
    for directory in os.listdir(path):
        spam = os.path.join(path,directory)
        if os.path.isdir(spam):
            shutil.rmtree(spam)
    
    # problem configuration
    problem_size = 2
    search_space = [[1, 25] for i in range(problem_size)]

    # algorithm configuration
    HMS = 10
    HMCR = 0.95
    PAR = 0.7
    bw = 0.05
    max_iter = 30 #1000

    repeat_iter = 50

    # execute the algorithm
    with open("results/hs_2D_wp_plot_runtime.txt", "a") as fout:
            t_start = time.time()

            for i in range(repeat_iter):
                t_start_a = time.time()
                best = search(search_space, max_iter, HMS, HMCR, PAR, bw, i)
                t_end_a = time.time()
                t_total_a = t_end_a - t_start_a
                fout.write(
                str(i) + " loop runtime:" + str(t_total_a / 60) + '[min]')
                fout.write("\n")

            t_end = time.time()
            t_total = t_end - t_start

            fout.write("\n")
            fout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
            fout.write(
                "  >> Total runtime:" + str(t_total / 60) + '[min]')
            fout.write("\n")

    