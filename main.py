import sys
from src.solver import Solver
from src.parsing import parse
from time import perf_counter

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = parse()
matrix = [x for y in matrix for x in y]
solver = Solver(matrix)


t_start = perf_counter()
print(solver.solve(matrix))
t_end = perf_counter() - t_start
print('Duration:' + ' %.4f second(s)' % (t_end))