import re
import sys

search_term = sys.argv[1]
f = sys.argv[2]

for line in open(f, 'r'):
    if re.search(search_term, line):
        print(line)