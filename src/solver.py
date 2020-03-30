import queue
from copy import deepcopy
import numpy as np
import math

class Solver:
    def __init__(self, graph, end_condition):
        self.graph = graph
        self.len = math.floor(math.sqrt(len(graph)))
        self.size = len(graph)
        self.zero = self.coor_zero(graph)
        self.goal = self.get_goal(graph)
        self.end_condition = end_condition

    def get_goal(self, graph):
        goal = [0] * self.len * self.len
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x, y, c = 0, -1, 1
        for i in range(self.len * 2 - 2):
            for j in range((self.len * 2 - i) // 2):
                x += dx[i % 4]
                y += dy[i % 4]
                goal[x * self.len + y] = c
                c += 1
        print('goal : ', goal)
        return goal

    """ get index of empty tile """

    def coor_zero(self, graph):
        for i in range(len(graph)):
            if graph[i] == 0:
                return i

    """ g == number of step taken, h = heuristic cost, f == g + h"""

    def get_opposite_move(self, move):
        if move == "L":
            return "R"
        if move == "R":
            return "L"
        if move == "U":
            return "D"
        if move == "D":
            return "U"

    # def     print_graph(self, graph):
    #     print()
    #     [print(x) for x in graph]

    """ adds 65 ('A' in ascii) to make the hash printable """
    def get_hash(self, graph):
        return ''.join([chr(x + 65) for x in graph])

    def solve(self, graph, heuristic):

        q = queue.PriorityQueue()
        h = heuristic(graph, self.goal, self.len)
        ghash = self.get_hash(graph)
        seen = {}
        q.put((h, 0, h, [""], self.zero, graph, ghash))
        while not q.empty():
            
            f, g, h, moves, x, graph, ghash = q.get()
            if ghash in seen:
                continue
            else:
                seen[ghash] = f

            if self.end_condition(h, self.goal, graph):
                print(graph)
                return moves[1:]

            for X, move in (x + 1, "R"), (x - 1, "L"), (x + self.len, "D"), (x - self.len, "U"):    
                if 0 <= X < self.size and move != self.get_opposite_move(moves[-1]):
                    new_graph = graph[:]
                    new_graph[x], new_graph[X] = new_graph[X], new_graph[x]
                    ghash = self.get_hash(new_graph)
                    if ghash not in seen:
                        new_h = heuristic(new_graph, self.goal, self.len)
                        new_h *= 1.0001
                        q.put((g + 1 + new_h, g + 1, new_h, moves + [move], X, new_graph, ghash))
                    else:
                        new_h = heuristic(new_graph, self.goal, self.len)
                        new_h *= 1.0001
                        if g + 1 + new_h < seen[ghash]:
                            q.put((g + 1 + new_h, g + 1, new_h, moves + [move], X, new_graph, ghash))
