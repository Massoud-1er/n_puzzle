import sys
from src.solver import Solver
from src.parsing import parse, print_usage, option
from time import perf_counter
from src.heuristic import heuristics

def	print_final_states(graph, moves, solver):
	print("Inital state: ", matrix)
	zero = solver.zero

	for i, m in enumerate(moves):
		if m == "L":
			x = zero - 1	
		if m == "R":
			x = zero + 1	
		if m == "U":
			x = zero - solver.len
		if m == "D":
			x = zero + solver.len
		matrix[x], matrix[zero] = matrix[zero], matrix[x]
		zero = x
		print("State {0:>2}:{1: <5}".format(i, ""), matrix)

def get_end_condition(h):
	if h == "djikstra":
		def end_djikstra(end, goal, graph):
			return goal == graph
		return end_djikstra
	else:
		def end_on_zero(h, _, __):
			return h == 0
		return end_on_zero

matrix = parse()

h, algo = option()

solver = Solver(matrix, get_end_condition(h))

t_start = perf_counter()
moves, MAX, total_node = solver.solve(matrix, heuristics[h], algo)

print_final_states(matrix, moves, solver)

print("Total number of states :", total_node)
print("Maximum number of states in memory :", MAX)
print('Number of moves :', len(moves))
t_end = perf_counter() - t_start
print('Duration:' + ' %.4f seconds' % (t_end))