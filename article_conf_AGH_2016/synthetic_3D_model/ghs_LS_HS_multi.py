#! usr/bin/env python3

# Changing 4 parameters

import random
import math
import os
import time
import csv
import shutil

from ecl_to_alg_multi import get_fitness_multi

algo_name = __file__.split(".")[0]

def objective_function(vector):
    w, x, y, z = vector
    result = float(get_fitness_multi(w, x, y, z))
    # result = random.choice([1000, 2000])
    with open("debug_ghs_LS_HS.txt", "w") as fout:
        fout.write("Type of result " + str(type(result)))
    return result

def rand_in_bounds(minimum, maximum):
    return random.randint(minimum, maximum)

def random_vector(search_space):
    # rand_vector = [random.randint(min(search_space[0][0]), max(search_space[0][1]))]
    rand_vector = [random.choice(search_space[0]),
                    random.choice(search_space[1]),
                    random.choice(search_space[2]),
                    random.choice(search_space[3])]
    return rand_vector

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
                if i in [0,1]:
                    value = best["vector"][random.randint(0, 1)]
                else:
                    value = best["vector"][random.randint(2, 3)]
            if value < min(search_space[i]):
                value = min(search_space[i])
            if value > max(search_space[i]):
                value = max(search_space[i])

            vector[i] = value
        else:
            vector = random_vector(search_space)

    return {"vector": vector}

def search(search_space, algo_iter, algo_conf, total):
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

        path, path2 = check_io_result(check_io_data(), total)

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


def check_io_data():
    data = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(data):
        os.mkdir(data)
    return data

def check_io_start():
    algo = os.path.join(check_io_data(), algo_name)
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
    return runtime


def check_io_result(data_path, total):
    algo = os.path.join(check_io_data(), algo_name)
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
    return path, path2


if __name__ == "__main__":
    runtime = check_io_start()

    # problem configuration
    # problem_size = 1
    # search_space = [[1, 30] for i in range(problem_size)]


    # search_space = [[100, 500], [100, 500], [10, 55], [10, 55]]
    search_space = [[x for x in range(100, 500, 100)],
                    [x for x in range(100, 500, 100)],
                    [x for x in range(10, 55, 5)],
                    [x for x in range(10, 55, 5)]]

    # search_space = [[100, 500], [100, 500], [10, 55], [10, 55]]

    # variable_conf = {
    #     "oil_prod": [[i] for i in range(400, 500, 100)],
    #     "water_inj": [[i] for i in range(100, 500, 100)],
    #     "time_HS": [[i] for i in range(10, 55, 5)],
    #     "time_LS": [[i] for i in range(10, 55, 5)]
    # }

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
            best = search(search_space, algo_iter, algo_conf, i)
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
