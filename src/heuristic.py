""" global array kep in memory for performance. """
goal_x = []
goal_y = []

index_x = []
index_y = []

goal_col = []
goal_row = []

""" helper function to keep in memory X and Y goal for every values. 

    Keeps goal indices to calculate manhattan distance.
    Keeps goal colomn and goal row to calculate linear conflict."""

def memorize_goal(goal, length):
    cols = [[0 for x in range(length)] for x in range(length)]
    rows = [[0 for x in range(length)] for x in range(length)]
    for i in range(len(goal)):
        x = goal.index(i) % length
        y = goal.index(i) // length
        
        idx_x = i % length
        idx_y = i // length

        rows[y][x] = i
        cols[x][y] = i
        
        goal_x.append(x)
        goal_y.append(y)

        index_x.append(idx_x)
        index_y.append(idx_y)
    
    for x in rows:
        goal_row.append(x)
    for x in cols:
        goal_col.append(x)

""" Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

def manhattan(graph, goal, length):
    total = 0
    if not len(goal_x) or not len(goal_y):
        memorize_goal(goal, length)
    for i in range(len(graph)):
        if graph[i]:
            total += abs(index_x[i] - goal_x[graph[i]]) + abs(index_y[i] - goal_y[graph[i]])
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

""" Linear Conflict """

""" If Axis is true, checks row otherwise checks colomns. """

def check_axis(val, index, axis, graph):
    total = 0
    if axis:
        for j in goal_row[index]:
            if j != 0 and j != val and index_y[graph.index(j)] is index:
                if (index_x[graph.index(j)] > goal_x[j] and index_x[graph.index(val)] < goal_x[val]) \
                    or (index_x[graph.index(j)] < goal_x[j] and index_x[graph.index(val)] > goal_x[val]):
                    total += 2
    else:
        for j in goal_col[index]:
            if j != 0 and j != val and index_x[graph.index(j)] is index:
                if (index_y[graph.index(j)] > goal_y[j] and index_y[graph.index(val)] < goal_y[val]) \
                    or (index_y[graph.index(j)] < goal_y[j] and index_y[graph.index(val)] > goal_y[val]):
                    total += 2
    return total

def linear_conflict(graph, goal, _):
    total = 0
    for i in range(len(graph)):
       if graph[i]:
           x = index_x[i]
           y = index_y[i]
           _goal_x = goal_x[graph[i]]
           _goal_y = goal_y[graph[i]]

           if y == _goal_y:
               total += check_axis(graph[i], y, True, graph)
           if x == _goal_x:
               total += check_axis(graph[i], x, False, graph)
    return total

def LC(graph, goal, length):
    return manhattan(graph, goal, length) + linear_conflict(graph, goal, length)

heuristics = {
    'hamming':      hamming,
    'manhattan':    manhattan,
    'djikstra':    djikstra,
    'conflict':    LC
}
