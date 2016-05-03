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

# from ecl_to_alg import get_fitness
from ecl_to_alg_sensivity_v2 import get_fitness


def objective_function(i, j, k, l, m, n, o):
    return float(get_fitness(i, j, k, l, m, n, o))

if __name__ == "__main__":
    # clean directories/files
    if os.path.exists('results/sensivity_run_v2.result'):
        os.remove('results/sensivity_run_v2.result')

    variable = "oil_prod"

    # problem configuration
    problem_size = [[i] for i in range(100, 1000, 100)]
    # print(problem_size)

    variable_conf = {
        "oil_prod": [i for i in range(100, 500, 100)],
        "water_inj": [i for i in range(100, 500, 100)],
        "time_HS": [i for i in range(10, 50, 10)],
        "time_LS": [i for i in range(10, 50, 10)],
        "op_bottom_con": [2, 3],
        "inj_top_con": [1, 2],
        "inj_bottom_con": [2, 3]
    }

    for i in variable_conf["oil_prod"]:
        for j in variable_conf["water_inj"]:
            for k in variable_conf["time_HS"]:
                for l in variable_conf["time_LS"]:
                    for m in variable_conf["op_bottom_con"]:
                        for n in variable_conf["inj_top_con"]:
                            for o in variable_conf["inj_bottom_con"]:
                                with open("results/sensivity_run_v2.result", "a") as fout:
                                    best = objective_function(i, j, k, l, m, n, o)
                                    fout.write("Parameter: " + " ")
                                    fout.write("oil_prod " + str(i) + " | ")
                                    fout.write("water_inj " + str(j) + " | ")
                                    fout.write("time_HS " + str(k) + " | ")
                                    fout.write("time_LS " + str(l) + " | ")
                                    fout.write("op_bottom_con " + str(m) + " | ")
                                    fout.write("inj_top_con " + str(n) + " | ")
                                    fout.write("inj_bottom_con " + str(o) + " | ")
                                    fout.write("Result: " + str(best))
                                    fout.write("\n")
                                    raise()

    # for var in variable_conf:
    #     for i in var:
    #         with open("results/sensivity_run.txt", "a") as fout:
    #             best = objective_function_single(i, var)
    #             fout.write("Parameter: " + var + str(i) + " | Result " + str(best))
    #             fout.write("\n")
