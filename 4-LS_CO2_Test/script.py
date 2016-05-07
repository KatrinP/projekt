import sys


def main(keyword, x, y, z):
    with open("blocks.txt", "w") as fout:
        fout.write(keyword + '\n')
        for i in range(1, int(x) + 1):
            for j in range(1, int(y) + 1):
                for k in range(1, int(z) + 1):
                    fout.write(str(i) + ' ' + str(j) + ' ' + str(k) + ' ' + "/" + "\n")
        fout.write("/")


if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except IndexError as e:
        print("IndexError")
        print("Correct format is: python script.py [keyword] [i] [j] [k]")
