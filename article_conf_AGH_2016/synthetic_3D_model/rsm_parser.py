import sys
import re


class RSM:
    def __init__(self):
        self.date = None
        self.run_nb = 0
        self.runs = []
        self.attributes = []


class Run:
    def __init__(self):
        self.order = 0
        self.attributes = []
        self.attributes_set = False
        self.unit_set = False
        self.well_names_set = False
        self.header_end = False


class Attribute:
    def __init__(self, name):
        self.name = name
        self.unit = None
        self.values = []
        self.well_name = None


def read_rsm_file(file_path):
    rsm = RSM()
    with open(file_path, "r") as rsm_file:
        _ = rsm_file.readline()
        new_run = Run()
        for line in rsm_file:
            if not line:
                continue
            elif re.match(r'^1', line):
                rsm.runs.append(new_run)
                rsm.attributes.extend(new_run.attributes)
                new_run = Run()
                rsm.run_nb += 1
            elif "SUMMARY OF RUN" in line:
                found = re.search(r'DATESTAMP (\d{2}-.{3}-\d{4})', line)
                if found:
                    rsm.date = found.group(1)
            elif not re.search(r'-+', line) and not new_run.attributes_set:
                new_run.attributes_set = True
                line = re.sub(r'  +', ' ', line)
                line_parsed = line.strip().split(" ")
                for attribute in line_parsed:
                    new_attribute = Attribute(attribute)
                    new_run.attributes.append(new_attribute)
            elif not re.search(r'-+', line) and not new_run.unit_set:
                new_run.unit_set = True
                line = re.sub(r'  +', ' ', line)
                line_parsed = line.strip().split(" ")
                for i, unit in enumerate(line_parsed):
                    new_run.attributes[i].unit = unit
            elif re.search(r'-+', line) \
                    and new_run.attributes_set \
                    and new_run.unit_set \
                    and not new_run.header_end:
                new_run.header_end = True
            elif re.search(r'-+', line):
                pass
            #elif not re.search(r'^-+$', line) and not new_run.well_names_set:
            #    new_run.well_names_set = True
                # line_parsed = line.split(" ")
                # for i, well_name in enumerate(line_parsed):
                #     new_run.attributes[i].well_name = well_name
            elif new_run.header_end:
                line = re.sub(r'  +', ' ', line)
                line_parsed = line.strip().split(" ")
                for i, value in enumerate(line_parsed):
                    new_run.attributes[i].values.append(value)

        rsm.runs.append(new_run)
        rsm.attributes.extend(new_run.attributes)
        rsm.run_nb += 1
    return rsm


def get_last_value_of_attribute(rsm, attribute_name):
    found = [e for e in rsm.attributes if getattr(e, "name") == attribute_name]
    try:
        value = found[0].values[-1]
    except IndexError:
        print("ERROR: The attribute with given name was not found.")
        value = None
    return value


def get_value_of_attribute_at_given_position(rsm, attribute_name, position):
    found = [e for e in rsm.attributes if getattr(e, "name") == attribute_name]
    try:
        value = found[0].values[position]
    except IndexError:
        print("ERROR: The attribute with given name was not found.")
        value = None
    return value



if __name__ == '__main__':
    rsm_path = sys.argv[1]
    rsm = read_rsm_file(rsm_path)
    print(get_last_value_of_attribute(rsm, "FOPT"))
    print(get_value_of_attribute_at_given_position(rsm, "WWPR", 1))