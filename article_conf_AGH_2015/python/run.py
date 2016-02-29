import os
import sys
import time


def main():
    '''run script eclrun.py file from cmd in windows'''

    # simulation_program = 'e300'
    # for argv in sys.argv:
        # simulation_program = argv[0]

    # print(sys.argv[1])
    # time.sleep(5)
    simulation_program = sys.argv[1]

    # sim_case_dir = 'c:'+os.sep+'ecl'+os.sep+'sim_case'+os.sep+'sim1D'
    sim_case_dir = os.getcwd()

    sim_case_list = [fil
             for fil in os.listdir(sim_case_dir) if fil.endswith(".DATA")]
    # print(sim_case_list)

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
        t_start = time.time()
        main()
        t_end = time.time()
        t_total = t_end - t_start
        print("Total runtime [min]: ", t_total/60)

    except KeyboardInterrupt:
        sys.exit(1)