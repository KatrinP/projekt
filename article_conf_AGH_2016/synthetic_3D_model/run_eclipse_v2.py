# No logging to runtime file

import os
import sys
import time


def run():
    '''run script eclrun.py file from cmd in windows'''

    simulation_program = 'eclipse'
    sim_case_dir = os.path.join(os.getcwd(), 'sim_case')
    # print(sim_case_dir)
    sim_case_list = [
        fil for fil in os.listdir(sim_case_dir) if fil.endswith(".DATA")]

    for case in sim_case_list:
        run_command = "{0} {1} {2}".format('eclrun', simulation_program,
                                           sim_case_dir + os.sep + case)
        if os.system(run_command) == 0:
            print("============================================")
            print('{0} was run successfully in {1}'.format(case,
                                                           simulation_program))
        else:
            sys.exit('SIMULATION FAILED')


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(1)
