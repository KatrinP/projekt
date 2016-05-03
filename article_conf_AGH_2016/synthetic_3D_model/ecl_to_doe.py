import shutil
import os
import fileinput
import subprocess

def get_fitness(factors):

    print(factors)
    try:
        os.remove(sim_case_tmp)
    except:
        pass

    sim_case_dir = os.path.join(os.getcwd(), 'sim_case')
    shutil.copy("BASE_doe.tmp", sim_case_dir)
    sim_case = os.path.join(sim_case_dir, "BASE_doe.tmp")
    sim_case_tmp = os.path.join(sim_case_dir, "BASE.DATA")
    shutil.copy(sim_case, sim_case_tmp)

    run_eclipse = 'run_eclipse.py'
    result = []

    for factor,value in factors.items():
        print(factor, value)
        with fileinput.FileInput(sim_case_tmp, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(factor, value), end='')

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
                result = line.split()[3]
                # print(line)
            # for i, line in enumerate(fin):
                # print(i, line)
                # if i == 21:
                    # result = line.split()[4]
    else:
        print("RSM not yet created, run simulation first")


    return result
