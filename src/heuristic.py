""" import sub operator to calculate manhattan distance more efficiently """
from operator import sub

""" helper function to keep in memory X and Y goal for every values. """
goal_x = []
goal_y = []

def memorize_goal(goal, length):
    for i in range(len(goal)):
        x = goal.index(i) % length
        y = goal.index(i) // length
        goal_x.append(x)
        goal_y.append(y)

""" Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

def manhattan(graph, goal, length):
    total = 0
    if not len(goal_x) or not len(goal_y):
        memorize_goal(goal, length)
    for i in range(len(graph)):
        if graph[i]:
            x = goal_x[graph[i]]
            y = goal_y[graph[i]]
            total += abs(i % length - x) + abs(i // length - y)
    return total

""" The Hamming distance is the total number of misplaced tiles."""

def hamming(graph, goal, _):
    total = 0
    for i in range(len(graph)):
        if graph[i]:
            total += int(goal.index(graph[i]) != i)
    return total

""" Djikstra """

def djikstra(graph, goal, _):
    return 0


heuristics = {
    'hamming':      hamming,
    'manhattan':    manhattan,
    'djikstra':    djikstra
}
