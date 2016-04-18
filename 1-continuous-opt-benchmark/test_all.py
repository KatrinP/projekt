# coding: utf-8
#! usr/bin/env python3

import time, os, glob, sys, shutil
from statistics import mean, median, stdev

from modules import *


# problem configuration
problem_size = 3
search_space = [[-5.12, 5.12] for i in range(problem_size)]

# algorithm configuration common for all
HMS = 20
max_iter = 100

# HS
HMCR = 0.95
PAR = 0.7
bw = 0.05

# GHS
PARmin = 0.4
PARmax = 0.9

# test conf
total = 1000

# execute the algorithm

filenames = glob.glob('modules/*.py')

lst = []
for files in filenames:
    lst.append(files[8:].split('.')[0])

lst.pop(-1)

best_list_total = []
best_list_total_ra = []

path=os.path.join(os.getcwd(), 'data')
for directory in os.listdir(path):
    if os.path.exists(os.path.join(path, directory)):
        shutil.rmtree(os.path.join(path, directory))

if os.path.exists('results.txt'):
    os.remove('results.txt')

with open('results.txt', "a") as results_file:
    for file in lst:
        text_file = file + ".txt"


        if os.path.exists(os.path.join('results',text_file)):
            os.remove(os.path.join('results',text_file))
        with open(os.path.join('results',text_file), "a") as fout:
            fout.write('Iteration;fitness')#;vectors')
            fout.write("\n")

            best_list = []

            t_start = time.time()
            for i in range(total):
                if file.startswith("g"):
                    best = eval(file).search(search_space, max_iter, HMS, HMCR, PARmin, PARmax, problem_size, i)
                else:
                    best = eval(file).search(search_space, max_iter, HMS, HMCR, PAR, bw, problem_size, i)
                    
                fout.write(str(i) + ';' + str(best['fitness']))
                # fout.write(';' + str(best['vector']))
                fout.write("\n")

                best_list.append(best['fitness'])
                # print(best_list)

            t_end = time.time()
            t_total = t_end - t_start

            print(file + " >> Total runtime: {:03.2f} [sec]".format(t_total))
            print(file + " >> Best result from {} iterations is {}".format(total, min(best_list)))
            print(file + " >> Mean {} | stdev {} | median {}".format(mean(best_list), stdev(best_list), median(best_list)))
            results_file.write(file + " >> Total runtime: "+str(t_total)+ " [sec] \n")
            results_file.write(file + " >> Best result from "+str(total)+" iterations is "+str(min(best_list))+ '\n')
            results_file.write(file + " >> Mean "+str(mean(best_list))+" | stdev "+str(stdev(best_list))+" | median "+str(median(best_list)) + '\n')
            results_file.write('\n')

        if "ra" not in file:
            best_list_total.append(min(best_list))
        else:
            best_list_total_ra.append(min(best_list))

    print("\n >> Overall best from sphere seems to be {}".format(min(best_list_total)))
    print("\n >> Overall best from rastrigin seems to be {}".format(min(best_list_total_ra)))

    results_file.write("\n >> Overall best from sphere seems to be {}".format(min(best_list_total)))
    results_file.write("\n >> Overall best from rastrigin seems to be {}".format(min(best_list_total_ra)))