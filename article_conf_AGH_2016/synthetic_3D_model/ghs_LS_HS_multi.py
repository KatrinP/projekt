#! usr/bin/env python3

# Changing 4 parameters

import random
import math
import os
import time
import csv
import shutil

from ecl_to_alg_sensivity import get_fitness_sensivity


def objective_function(w, x, y, z):
    result = float(get_fitness(w, x, y, z))
    with open("debug_ghs_LS_HS.txt", "w") as fout:
        fout.write("Type of result " + str(type(result)))
    return result

def rand_in_bounds(minimum, maximum):
    return random.randint(minimum, maximum)

def random_vector(search_space):
    rand_vector = [random.randint(min(search_space[0][0]), max(search_space[0][1]))]
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

def create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, algo_iter, gn):
    limit = len(search_space)
    vector = [0 for i in range(limit)]

    PARmod = PARmin + ((PARmax - PARmin)/algo_iter)*gn

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

def search(search_space, algo_iter, algo_conf, total, data_path):
    HMS, HMCR, PARmin, PARmax = algo_conf
    memory = initialize_harmony_memory(HMS, search_space)
    best = memory[0]
    for i in range(algo_iter):
        harm = create_harmony(search_space, memory, best, HMCR, PARmin, PARmax, algo_iter, i)
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

        check_io_result(data_path, total)

        # write fitness
        with open(os.path.join(path, 'fitness.csv'), 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([i,best['fitness']])

        ## write coordinates
        with open(os.path.join(path2, 'vector.csv'), 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([i,best['fitness'],best['vector']])

    return best


def check_io_start(algo_name):
    data = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(data):
        os.mkdir(data)

    algo = os.path.join(data, algo_name)
    if not os.path.exists(algo):
        os.mkdir(algo)

    for directory in os.listdir(algo):
        spam = os.path.join(algo,directory)
        if os.path.isdir(spam):
            shutil.rmtree(spam)

    results = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(results):
        os.mkdir(results)
    runtime = os.path.join(results, algo_name + "_runtime.txt")
    ## POSSIBLE UNNECCESSARY ??
    if os.path.exists(runtime):
        os.remove(runtime)
    return runtime, data


def check_io_result(data_path, total):
    fitness = os.path.join(algo, 'fitness')
    if not os.path.exists(fitness):
        os.mkdir(fitness)
    path = os.path.join(fitness, str(total))
    if not os.path.exists(path):
        os.mkdir(path)

    vectors = os.path.join(algo, 'vectors')
    if not os.path.exists(vectors):
        os.mkdir(vectors)
    path2 = os.path.join(vectors, str(total))
    if not os.path.exists(path2):
        os.mkdir(path2)


if __name__ == "__main__":
    runtime, data_path = check_io_start("ghs_LS_HS")

    # problem configuration
    # problem_size = 1
    # search_space = [[1, 30] for i in range(problem_size)]


    # search_space = [[100, 500], [100, 500], [10, 55], [10, 55]]
    search_space = [[x for x in range(100, 500, 100)],
                    [x for x in range(100, 500, 100)],
                    [x for x in range(10, 55, 5)],
                    [x for x in range(10, 55, 5)]]

    search_space = [[100, 500], [100, 500], [10, 55], [10, 55]]

    variable_conf = {
        "oil_prod": [[i] for i in range(400, 500, 100)],
        "water_inj": [[i] for i in range(100, 500, 100)],
        "time_HS": [[i] for i in range(10, 55, 5)],
        "time_LS": [[i] for i in range(10, 55, 5)]
    }

    # algorithm configuration
    # [HMS, HMCR, PARmin, PARmax]
    algo_conf = [5, 0.95, 0.4, 0.9]
    algo_iter = 30

    repeat_iter = 30

    t_start = time.time()
    for i in range(repeat_iter):
        with open(runtime, "a") as fout:
            t_start_a = time.time()
            # execute the algorithm
            best = search(search_space, algo_iter, algo_conf, i, data_path)
            t_end_a = time.time()
            t_total_a = t_end_a - t_start_a
            minute, second = divmod(t_total_a, 60)
            fout.write("Iteration " + str(i+1) + "/" + str(repeat_iter))
            fout.write(" runtime:" + "{:2.0f}".format(minute) + 'min')
            fout.write(" {:2.2f}".format(second) + 'sec')
            fout.write("\n")
            print("best", best)

    with open(runtime, "a") as fout:
        t_end = time.time()
        t_total = t_end - t_start
        fout.write("\n")
        fout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        fout.write("  >> Total runtime:" + str(t_total / 60) + '[min]')
        fout.write("\n")
