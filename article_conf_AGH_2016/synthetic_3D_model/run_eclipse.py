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

    with open("results/eclipse_runtime_log.txt", "a") as fout:

        for case in sim_case_list:
            run_command = "{0} {1} {2}".format('eclrun', simulation_program,
                                               sim_case_dir + os.sep + case)
            t_start = time.time()
            if os.system(run_command) == 0:
                print("============================================")
                print('{0} was run successfully in {1}'.format(case,
                                                               simulation_program))
                t_end = time.time()
                t_total = t_end - t_start
                # print("-------------------------------------")
                # print(case + " runtime [min]: ", t_total / 60)
                fout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
                fout.write(
                    "  " + case + "  runtime:" + str(t_total / 60) + '[min]')
                fout.write("\n")
            else:
                sys.exit('SIMULATION FAILED')


if __name__ == "__main__":
    try:
        t_start = time.time()
        run()
        t_end = time.time()
        t_total = t_end - t_start
        print("#####################")
        print("Total runtime [min]: ", t_total / 60)

    except KeyboardInterrupt:
        sys.exit(1)
