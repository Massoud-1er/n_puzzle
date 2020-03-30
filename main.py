import sys
from src.solver import Solver
from src.parsing import parse

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

matrix = parse()
solver = Solver(matrix)

print(solver.solve(matrix))