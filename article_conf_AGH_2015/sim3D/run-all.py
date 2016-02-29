import os
import sys
import time



def main():
    '''run script eclrun.py file from cmd in windows'''

    simulation_program = sys.argv[1]
    message = sys.argv[2]

    sim_case_dir = os.getcwd()

    sim_case_list = [fil
             for fil in os.listdir(sim_case_dir) if fil.endswith(".DATA")]

    with open("aa_log.txt", "a") as fout:   

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
                fout.write(time.strftime("%Y-%m-%d %H:%M:%S"))
                fout.write("  " + case + "  runtime was [min]:" + str(t_total/60)+'\n')
                fout.write(message)
                fout.write("\n\n")

            else:
                sys.exit('SIMULATION FAILED')



if __name__ == "__main__":
    try:
        t_start = time.time()
        main()
        t_end = time.time()
        t_total = t_end - t_start
        print("#####################")
        print("Total runtime [min]: ", t_total/60)

    except KeyboardInterrupt:
        sys.exit(1)