import sys


def main(keyword, x, y, z):
    with open("blocks", "w") as fout:
        fout.write(keyword + '\n')
        for i in range(1, int(x) + 1):
            for j in range(1, int(y) + 1):
                for k in range(1, int(z) + 1):
                    fout.write(str(i) + ' ' + str(j) + ' ' + str(k) + ' ' + "/" + "\n")
                    # print("BSCN", i, j, k)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
