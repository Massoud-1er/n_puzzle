import sys
from .solver import Solver

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = []

def parse():
    matrix = []
    size = 0
    for l in lines:
        line = l.split('#')
        if line[0].isnumeric():
            size = int(line[0])
        elif size > 0:
            raw = line[0].split(' ')
            if len(raw) >= size:
                matrix_raw = []
                for val in raw:
                    if val.isnumeric() and len(matrix_raw) <= size:
                        matrix_raw.append(int(val))
                print(matrix_raw)
                matrix.append(matrix_raw)
    print(matrix)
    return matrix
