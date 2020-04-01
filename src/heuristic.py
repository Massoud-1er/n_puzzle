from math import sqrt, floor
from itertools import permutations

""" global array kep in memory for performance. """
goal_coor = { 'x': [], 'y': [] }

indices = { 'x': [], 'y': [] }

goals = { 'row': [], 'col': [] }

conflict = {}

_len = 0

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
        
        goal_coor['x'].append(x)
        goal_coor['y'].append(y)

        indices['x'].append(idx_x)
        indices['y'].append(idx_y)
    
    for x in rows:
        goals['row'].append(x)
    for x in cols:
        goals['col'].append(x)

""" Manhattan Distance of a tile is the distance or the number of slides/tiles away it is from it’s goal state.
Thus, for a certain state the Manhattan distance will be the sum of the Manhattan distances of all the tiles except the blank tile."""

def manhattan(graph, goal, length):
    total = 0
    if not len(goal_coor['x']) or not len(goal_coor['y']):
        memorize_goal(goal, length)
    for i in range(len(graph)):
        if graph[i]:
            total += abs(indices['x'][i] - goal_coor['x'][graph[i]]) + abs(indices['y'][i] - goal_coor['y'][graph[i]])
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

""" Check for linear conflict row by row. """

def check_row(row, _goal_row, index, axis):
    total = 0
    for i, x in enumerate(row):
        if x and goal_coor['y'][x] is index:
            for j, y in enumerate(row):
                if i is not j and y and goal_coor['y'][y] is index:
                    if i < j and goal_coor['x'][x] > goal_coor['x'][y] \
                        or i > j and goal_coor['x'][x] < goal_coor['x'][y]:
                        total += 1
    return total

""" Keeps in memory value of manhattan conflict for each row. """

def manhattan_row(row, index):
    total = 0
    for i, val in enumerate(row):
        if val:
            total += abs(i - goal_coor['x'][val]) + abs(index - goal_coor['y'][val])
    return total

def linear_conflict(graph, goal, length):
    total = 0
    for i in range(_len):
        row = tuple([graph[i * _len + x] for x in range(_len)])
        col = tuple([graph[i + x * _len] for x in range(_len)])
        
        if row not in conflict['row'][i]:
            conflict['row'][i][row] = check_row(row, goals['row'][i], i, 'row')
            conflict['row'][i][row] += manhattan_row(row, i)
            total += conflict['row'][i][row]
        else:
            total += conflict['row'][i][row]
            
        if col not in conflict['col'][i]:
            conflict['col'][i][col] = check_row(col, goals['col'][i], i, 'col')
            total += conflict['col'][i][col]
        else:
            total += conflict['col'][i][col]
    return total

""" Keeps values in memory and calls linear conflict """

def LC(graph, goal, length):
    if 'row' not in conflict or 'col' not in conflict:
        conflict['row'] = [{} for x in range(length)]
        conflict['col'] = [{} for x in range(length)]
        global _len
        _len = floor(sqrt(len(graph)))
    if not len(goal_coor['x']) or not len(goal_coor['y']):
        memorize_goal(goal, length)

    return linear_conflict(graph, goal, length)

heuristics = {
    'hamming':      hamming,
    'manhattan':    manhattan,
    'djikstra':     djikstra,
    'conflict':     LC
}
