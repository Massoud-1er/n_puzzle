import sys
from .solver import Solver

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = []

def print_usage():
    print('wrong parameter: python3 main.py < input_file.txt')
    print('/t/t/t/tThe options are as follows:')
    print('/t/t/t/t-h [ manhattan (default), djikstra, hamming, conflict ]')
    print('/t/t/t/t-ida Iterative Deepening A Star search Algorithm instead of default A Star Algorithm')
    exit(1)

def parse():
    matrix = []
    size = 0
    solvable = lines.pop(0)
    
    if "unsolvable" in solvable:
        print("unsolvable !")
        exit(0)

    for l in lines:
        line = l.split('#')[0].rstrip()
        if line.isnumeric() and size == 0:
            size = int(line)
        elif size > 0:
            raw = line.split(' ')
            count = 0
            if len(raw) != size:
                print_usage()
            for val in raw:
                if val.isnumeric():
                    matrix.append(int(val))
                else:
                    print_usage()
                count += 1
            if count != size:
                print_usage()
        else:
            print_usage()
    print(matrix)
    exit(1)
    return matrix
