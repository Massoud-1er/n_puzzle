import sys
from src.solver import Solver
from src.parsing import parse
from time import perf_counter
from src.heuristic import heuristics

def get_end_condition(h):
	if h == "djikstra":
		def end_djikstra(end, goal, graph):
			return goal == graph
		return end_djikstra
	else:
		def end_on_zero(h, _, __):
			return h == 0
		return end_on_zero

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = parse()
matrix = [x for y in matrix for x in y]

h = "manhattan"
if len(sys.argv) > 1:
	if sys.argv[1] == "hamming":
		h = "hamming"
	elif sys.argv[1] == "djikstra":
		h = "djikstra"

solver = Solver(matrix, get_end_condition(h))

t_start = perf_counter()
moves, MAX, total_node = solver.solve(matrix, heuristics[h])
print('moves, MAX, total_node : ', moves, MAX, total_node)
t_end = perf_counter() - t_start
print('Duration:' + ' %.4f seconds' % (t_end))