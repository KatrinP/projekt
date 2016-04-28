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
from ecl_to_alg_sensivity import get_fitness_sensivity


def objective_function_single(vector, variable):
    result = float(get_fitness(vector, variable))
    with open("debug_ghs_LS_HS_plot.txt", "w") as fout:
        fout.write("Type of result " + str(type(result)))

    # result = random.choice([2000.13, 500.4, 5546.1, 1836.5, 222,
        # 1000, 1500, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
    return result

def objective_function_multi(i, j, k, l):
    return float(get_fitness_sensivity(i, j, k, l))

if __name__ == "__main__":
    # clean directories/files
    if os.path.exists('results/sensivity_run.txt'):
        os.remove('results/sensivity_run.txt')

    variable = "oil_prod"

    # problem configuration
    problem_size = [[i] for i in range(100, 1000, 100)]
    # print(problem_size)

    variable_conf = {
        "oil_prod": [[i] for i in range(100, 500, 100)],
        "water_inj": [[i] for i in range(100, 500, 100)],
        "time_HS": [[i] for i in range(10, 55, 5)],
        "time_LS": [[i] for i in range(10, 55, 5)]
    }

    for i in variable_conf["oil_prod"]:
        for j in variable_conf["water_inj"]:
            for k in variable_conf["time_HS"]:
                for l in variable_conf["time_LS"]:
                    with open("results/sensivity_run.txt", "a") as fout:
                        best = objective_function_multi(i, j, k, l)
                        fout.write("Parameter: " + " ")
                        fout.write("oil_prod " + str(i) + " | ")
                        fout.write("water_inj " + str(j) + " | ")
                        fout.write("time_HS " + str(k) + " | ")
                        fout.write("time_LS " + str(l) + " | ")
                        fout.write("Result: " + str(best))
                        fout.write("\n")

    # for var in variable_conf:
    #     for i in var:
    #         with open("results/sensivity_run.txt", "a") as fout:
    #             best = objective_function_single(i, var)
    #             fout.write("Parameter: " + var + str(i) + " | Result " + str(best))
    #             fout.write("\n")
