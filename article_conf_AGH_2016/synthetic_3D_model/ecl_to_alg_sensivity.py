import shutil
import os
import fileinput
import subprocess

def get_fitness_sensivity(i, j, k, l):
    sim_case_dir = os.path.join(os.getcwd(), 'sim_case')
    shutil.copy("BASE_sensivity_opt.tmp", sim_case_dir)
    sim_case = os.path.join(sim_case_dir, "BASE_sensivity_opt.tmp")
    sim_case_tmp = os.path.join(sim_case_dir, "BASE.DATA")
    run_eclipse = 'run_eclipse.py'

    message = 'HS test'
    result = []
    shutil.copy(sim_case, sim_case_tmp)

    textToSearch1 = "oil_prod"
    textToSearch2 = "water_inj"
    textToSearch3 = "time_HS"
    textToSearch4 = "time_LS"
    textToReplace1 = str(i[0])
    textToReplace2 = str(j[0])
    textToReplace3 = str(k[0])
    textToReplace4 = str(l[0])

############ DEBUG
    # if os.path.exists("vector_debug.txt"):
    #     os.remove('vector_debug.txt')
    # with open("vector_debug.txt", 'a') as fout:
    #     fout.write("vector: " + str(vector))
    #     fout.write('\n')
    #     fout.write('textToReplace: ' + textToReplace)
    #     fout.write('\n')
    #     fout.write('\n')
##############

    with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch1, textToReplace1), end='')
    with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch2, textToReplace2), end='')

    with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch3, textToReplace3), end='')

    with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch4, textToReplace4), end='')

    subprocess.call(['python', run_eclipse])

    if os.path.exists(os.path.join(sim_case_dir, "BASE.RSM")):
        rsm_file = os.path.join(sim_case_dir, "BASE.RSM")
        with open(rsm_file, 'r') as fin:
            with open("debug_ecl_to_alg.txt", "a") as fout:
                for line in fin:
                    pass
                fout.write(line)
                # fout.write("\n")
                # fout.write("Oil production: " + str(vector[0]))
                fout.write("\n")
                result = line.split()[2]
                # print(line)
            # for i, line in enumerate(fin):
                # print(i, line)
                # if i == 21:
                    # result = line.split()[4]
    else:
        print("RSM not yet created, run simulation first")

    os.remove(sim_case_tmp)

    return result
