import queue
from copy import deepcopy

class Solver:
    def __init__(self, graph):
        self.graph = graph
        self.len = len(graph)
        self.x, self.y = self.coor_zero(graph)

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
                if not graph[y][x]:
                    return x, y

    def get_updated_zero(self, moves):
        x = self.x
        y = self.y

        for m in moves:
            if m == "L":
                x -= 1
            elif m == "R":
                x += 1
            elif m == "U":
                y += 1
            elif m == "D":
                y -= 1

        return x, y
    
    def get_updated_graph(self, graph, moves):
        x = self.x
        y = self.y

        for m in moves:
            if m == "L":
                graph[y][x], graph[y][x - 1] = graph[y][x - 1], graph[y][x]
                x -= 1
            elif m == "R":
                graph[y][x], graph[y][x + 1] = graph[y][x + 1], graph[y][x]
                x += 1
            elif m == "U":
                graph[y][x], graph[y + 1][x] = graph[y + 1][x], graph[y][x]
                y += 1
            elif m == "D":
                graph[y][x], graph[y - 1][x] = graph[y - 1][x], graph[y][x]
                y -= 1

        return graph

    """ Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
    Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

    def manhattan_distance(self, graph):
        total = 0
        for i in range(self.len):
            for j in range(self.len):
                if graph[i][j]:
                    x = (graph[i][j] - 1) % self.len
                    y = (graph[i][j] - 1) // self.len
                    total += abs(x - j) + abs(y - i)
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

    def solve(self, graph):

        q = queue.PriorityQueue()
        h = self.manhattan_distance(graph)
        q.put((h, 0, h, [""]))

        while not q.empty():
            _, g, h, moves = q.get()
            x, y = self.get_updated_zero(moves)
            print('x, y : ', x, y)
            # if g == 1:
            #     exit()
            for X, Y, move in (x + 1, y, "R"), (x - 1, y, "L"), (x, y + 1, "U"), (x, y - 1, "D"):
                if 0 <= X < self.len and 0 <= Y < self.len and move != self.get_opposite_move(moves[-1]):
                    new_moves = moves[:]
                    new_moves.append(move)
                    new_graph = self.get_updated_graph(deepcopy(graph), new_moves)
                    if self.is_solved(new_graph):
                        print(new_moves)
                        return new_moves
                    print('h : ', h)
                    new_h = self.manhattan_distance(new_graph)
                    print('new_h : ', new_h)
                    self.print_graph(new_graph)
                    if new_h < h:
                        q.put((g + 1 + h, g + 1, h, new_moves))