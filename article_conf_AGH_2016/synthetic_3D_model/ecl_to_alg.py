import shutil
import os
import fileinput
import subprocess

def get_fitness(time_HS):
    sim_case_dir = os.path.join(os.getcwd(), 'sim_case')
    shutil.copy("BASE_origin.tmp", sim_case_dir)
    sim_case = os.path.join(sim_case_dir, "BASE_origin.tmp")
    sim_case_tmp = os.path.join(sim_case_dir, "BASE.DATA")
    run_eclipse = 'run_eclipse.py'

    message = 'HS test'
    result = []
    shutil.copy(sim_case, sim_case_tmp)

    textToSearch = 'time_LS'
    textToReplace = str(time_HS[0])

############ DEBUG
    # if os.path.exists("vector_debug.txt"):
    #     os.remove('vector_debug.txt')
    # with open("vector_debug.txt", 'a') as fout:
    #     fout.write("time_HS: " + str(time_HS))
    #     fout.write('\n')
    #     fout.write('textToReplace: ' + textToReplace)
    #     fout.write('\n')
    #     fout.write('\n')
##############

    with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')

    subprocess.call(['python', run_eclipse])

    if os.path.exists(os.path.join(sim_case_dir, "BASE.RSM")):
        rsm_file = os.path.join(sim_case_dir, "BASE.RSM")
        with open(rsm_file, 'r') as fin:
            with open("debug.txt", "w") as fout:
                for line in fin:
                    pass
                fout.write(line)
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