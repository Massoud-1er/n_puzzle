import sys
from src.solver import Solver
from src.parsing import parse

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = parse()
solver = Solver(matrix)
# print(matrix)
# print(solver.is_solved(matrix))
# print(solver.manhattan_distance(matrix))
print(solver.solve(matrix))