#! usr/bin/env python3

# Changing 2 parameters
# problem_size = 1
# search_space = [[1, 30] for i in range(problem_size)]

import random
import math
import os
import time
import csv
import shutil

from ecl_to_alg import get_fitness


def objective_function(vector):
    result = float(get_fitness(vector))
    with open("debug_ghs_LS_HS_plot.txt", "w") as fout:
        fout.write("Type of result " + str(type(result)))

    # result = random.choice([2000.13, 500.4, 5546.1, 1836.5, 222,
        # 1000, 1500, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
    return result

def rand_in_bounds(minimum, maximum):
    return random.randint(minimum, maximum)

def random_vector(search_space):
    rand_vector = [random.randint(min(search_space[0]), max(search_space[0]))]
    # banned_list = [[1,1], [25,25], [1,25], [25,1]]
    return rand_vector
    # if rand_vector not in banned_list:
    #     return rand_vector
    # else:
    #     return random_vector()

def create_random_harmony(search_space):
    harmony = {}
    harmony["vector"] = random_vector(search_space)
    harmony["fitness"] = objective_function(harmony["vector"])
    return harmony

def initialize_harmony_memory(HMS, search_space):
    memory = [create_random_harmony(search_space)
              for i in range(HMS)]
    # print(memory)
    #memory = sorted(memory, key=itemgetter('fitness'))
    memory = sorted(memory, key= lambda k: k["fitness"])
    return [memory[i] for i in range(HMS)]

def create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, max_iter, gn):
    limit = len(search_space)
    vector = [0 for i in range(limit)]

    PARmod = PARmin + ((PARmax - PARmin)/max_iter)*gn

    for i in range(limit):
        if random.random() < HMCR:
            value = memory[random.randint(0, len(memory)-1)]["vector"][i]
            if random.random() < PARmod:
                # value = value + rand_in_bounds(-1.0, 1.0)
                value = best["vector"][random.randint(0, limit-1)]
            if value < search_space[i][0]:
                value = search_space[i][0]
            if value > search_space[i][1]:
                value = search_space[i][1]

            vector[i] = value
        else:
            vector = random_vector(search_space)

    return {"vector": vector}

def search(search_space, max_iter, HMS, HMCR, PARmin, PARmax, total):
    memory = initialize_harmony_memory(HMS, search_space)
    best = memory[0]
    for i in range(max_iter):
        harm = create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, max_iter, i)
        # print(harm)
        harm["fitness"] = objective_function(harm["vector"])
        if harm["fitness"] > best["fitness"]:
            best = harm

        ## Penalty function for heavy time calculations
        # else:
        #     penalty += 1
        # if penalty >= 10:
        #     continue

        memory.append(harm)
        memory = sorted(memory, key= lambda k: k["fitness"])

        del memory[0]

        # write fitness
        path0 = os.path.join(os.getcwd(), 'data', 'ghs_LS_HS', 'fitness')
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
        path20 = os.path.join(os.getcwd(), 'data', 'ghs_LS_HS', 'vectors')
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
    if os.path.exists('results/ghs_LS_HS_plot_runtime.txt'):
        os.remove('results/ghs_LS_HS_plot_runtime.txt')

    path000 = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(path000):
        os.mkdir(path000)

    path00 = os.path.join(path000, 'ghs_LS_HS')
    if not os.path.exists(path00):
        os.mkdir(path00)
    path='data/ghs_LS_HS/'
    for directory in os.listdir(path):
        spam = os.path.join(path,directory)
        if os.path.isdir(spam):
            shutil.rmtree(spam)

    # problem configuration
    problem_size = 1
    search_space = [[1, 30] for i in range(problem_size)]

    # algorithm configuration
    HMS = 5
    # HMS = 1
    HMCR = 0.95
    PARmin = 0.4
    PARmax = 0.9
    max_iter = 30 #1000
    # max_iter = 1

    repeat_iter = 30
    # repeat_iter = 1

    # execute the algorithm
    path_results = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(path_results):
        os.mkdir(path_results)

    t_start = time.time()

    for i in range(repeat_iter):
        with open("results/ghs_LS_HS_plot_runtime.txt", "a") as fout:
            t_start_a = time.time()
            best = search(search_space, max_iter, HMS, HMCR, PARmin, PARmax, i)
            t_end_a = time.time()
            t_total_a = t_end_a - t_start_a
            minute, second = divmod(t_total_a, 60)
            fout.write("Iteration " + str(i+1) + "/" + str(repeat_iter))
            fout.write(" runtime:" + "{:2.0f}".format(minute) + 'min')
            fout.write(" {:2.2f}".format(second) + 'sec')
            fout.write("\n")
            print("best", best)

    with open("results/ghs_LS_HS_plot_runtime.txt", "a") as fout:
        t_end = time.time()
        t_total = t_end - t_start
        fout.write("\n")
        fout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        fout.write("  >> Total runtime:" + str(t_total / 60) + '[min]')
        fout.write("\n")
