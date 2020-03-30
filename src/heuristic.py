""" Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

def manhattan(graph, goal, length):
    total = 0
    for i in range(len(graph)):
        if graph[i]:
            y = goal.index(graph[i]) // length
            x = goal.index(graph[i]) % length
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
