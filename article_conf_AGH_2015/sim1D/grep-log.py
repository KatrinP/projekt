import re
import sys

def main():
    '''grep + log'''

    with open("aa_grep.txt", "w") as fout:

        search_term = sys.argv[1]
        f = sys.argv[2]

        fout.write("Pattern: " + search_term + "\n")
        fout.write("File: " + f + "\n\n")

        for line in open(f, 'r'):
            if re.search(search_term, line):
                fout.write(line)
                fout.write("")


if __name__ == "__main__":
    try:
        main()
        print("Done!")
    except KeyboardInterrupt:
        sys.exit(1)