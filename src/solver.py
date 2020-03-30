import queue
from copy import deepcopy
import numpy as np

class Solver:
    def __init__(self, graph):
        self.graph = graph
        self.len = len(graph)
        self.x, self.y = self.coor_zero(graph)
        self.goal = self.get_goal(graph)

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
        return goal


    def is_solved(self, graph):
        prev = graph[0][0]
        for i in range(self.len):
            for j in range(self.len):
                if graph[i][j] < prev:
                    return False
                prev = graph[i][j]
        return True

    def coor_zero(self, graph):
        for y in range(self.len):
            for x in range(self.len):
                if graph[y][x] == 0:
                    return x, y
    
    def get_updated_graph(self, graph, move, x, y):
        if move == "L":
            graph[y][x + 1], graph[y][x] = graph[y][x], graph[y][x + 1]
        elif move == "R":
            graph[y][x - 1], graph[y][x] = graph[y][x], graph[y][x - 1]
        elif move == "D":
            graph[y - 1][x], graph[y][x] = graph[y][x], graph[y - 1][x]
        elif move == "U":
            graph[y + 1][x], graph[y][x] = graph[y][x], graph[y + 1][x]

        return graph

    """ Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
    Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

    def manhattan_distance(self, graph):
        total = 0
        for i in range(self.len):
            for j in range(self.len):
                if graph[i][j]:
                    y = self.goal.index(graph[i][j]) // self.len
                    x = self.goal.index(graph[i][j]) % self.len
                    total += abs(j - x) + abs(i - y)
        return total
    
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

    def     print_graph(self, graph):
        print()
        [print(x) for x in graph]

    """ adds 65 ('A' in ascii) to make the hash printable """
    def get_hash(self, graph):
        return ''.join([chr(x + 65) for y in graph for x in y])

    def solve(self, graph):

        q = queue.PriorityQueue()
        h = self.manhattan_distance(graph)
        seen = {}
        seen[self.get_hash(graph)] = 0 + h
        q.put((h, 0, h, [""], self.x, self.y, graph))
        while not q.empty():
            _, g, h, moves, x, y, graph = q.get()

            for X, Y, move in (x + 1, y, "R"), (x - 1, y, "L"), (x, y + 1, "D"), (x, y - 1, "U"):    
                if 0 <= X < self.len and 0 <= Y < self.len and move != self.get_opposite_move(moves[-1]):
                    new_graph = self.get_updated_graph(deepcopy(graph), move, X, Y)
                
                    new_h = self.manhattan_distance(new_graph)
                    if new_h == 0:
                        self.print_graph(new_graph)
                        return moves[1:] + [move]
                    
                    # new_h *= 1.0005
                    ghash = self.get_hash(new_graph)
                    if ghash not in seen or g + 1 + new_h < seen[ghash]:
                        seen[ghash] = g + 1 + new_h
                        q.put((g + 1 + new_h, g + 1, new_h, moves + [move], X, Y, new_graph))