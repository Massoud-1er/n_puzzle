import sys
from .solver import Solver

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = []

def print_usage():
    print('wrong parameter: python3 main.py < input_file.txt')
    print('         The options are as follows:')
    print('         -h [ manhattan (default), djikstra, hamming, conflict ]')
    print('         -ida Iterative Deepening A Star search Algorithm instead of default A Star Algorithm')
    exit(1)

def option():
	h = "manhattan"
	algo = "a_star"
	try:
		for idx, arg in enumerate(sys.argv):
			if arg == '-h' and sys.argv[idx + 1] in heuristics.keys():
				h = sys.argv[idx + 1]

			elif arg == '-ida':
				algo = 'ida_star'
			
			elif sys.argv[idx - 1] != '-h' and arg != 'main.py':
				print_usage()

		return h, algo
	except:
		print_usage()

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
    return matrix
