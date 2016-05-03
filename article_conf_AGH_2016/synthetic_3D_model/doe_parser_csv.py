import csv
import sys

from ecl_to_doe import get_fitness

class Doe:
    def __init__(self):
        self.factors_nb = 0
        self.responses_nb = 0
        self.sth_else = 0
        self.types = []
        self.names = []
        self.runs = []
        self.delimiter = []


class Run:
    def __init__(self, std, run_nb):
        self.std = std
        self.run = run_nb
        self.other = {}
        self.factors = {}
        self.responses = {}


def get_response(doe):
    for run in doe.runs:
        run.responses["R1"] = get_fitness(run.factors)
    return(doe)


def write_csv(csv_path, doe):
    with open(csv_path, "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")

        csv_writer.writerow(doe.types)
        csv_writer.writerow(doe.names)
        csv_writer.writerow(doe.delimiter)

        for run in doe.runs:
            row = []
            #row.append(run.std)
            #row.append(run.run)
            for name in doe.names:
                try:
                    row.append(run.factors[name[2:]])
                except KeyError:
                    pass
                try:
                    row.append(run.responses[name])
                except KeyError:
                    pass
                try:
                    row.append(run.other[name])
                except KeyError:
                    pass
            csv_writer.writerow(row)


def read_csv(csv_path):
    doe = Doe()
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        doe.types = next(csv_reader)
        doe.names = next(csv_reader)
        doe.delimiter = next(csv_reader)

        doe.factors_nb = 0
        doe.responses_nb = 0
        sth_else = 0
        for type in doe.types:
            if "Factor" in type:
                doe.factors_nb += 1
            elif "Response" in type:
                doe.responses_nb += 1
            else:
                sth_else += 1

        for line in csv_reader:
            new_run = Run(line[0], line[1])
            for i in range(0, sth_else):
                new_run.other[doe.names[i]] = line[i]

            for i in range(sth_else, doe.factors_nb + sth_else):
                new_run.factors[doe.names[i][2:]] = line[i]

            for i in range(sth_else + doe.factors_nb, doe.responses_nb + doe.factors_nb + sth_else):
                new_run.responses[doe.names[i]] = line[i]

            doe.runs.append(new_run)

    return doe


if __name__ == '__main__':
    csv_path = sys.argv[1]
    doe = read_csv(csv_path)
    doe = get_response(doe)

    write_csv(csv_path, doe)
