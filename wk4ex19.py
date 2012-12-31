# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    value = [[[999 for row in col] for col in grid] for dir in forward]
    policy3D = [[[999 for row in col] for col in grid] for dir in forward]
    policy2D = [[' ' for row in col] for col in grid]

    def compute_value_recurse(x, y, d, c):
        value[d][x][y] = c

        for a in range(len(action)):
            d2 = (d - action[a]) % len(forward)
            (dx,dy) = forward[d2]
            x2 = x - dx
            y2 = y - dy
            if (x2 in range(len(grid)) and y2 in range(len(grid[0]))):
                c2 = c + cost[a]
                if (grid[x2][y2] != 1 and value[d2][x2][y2] > c2):
                    policy3D[d2][x2][y2] = a
                    compute_value_recurse(x2,y2,d2,c2)

    for d in range(len(forward)):
        compute_value_recurse(goal[0], goal[1], d, 0)

    def traverse(x,y,d):
        if (x == goal[0] and y == goal[1]):
            policy2D[x][y] = '*'
        else:
            a = policy3D[d][x][y]
            if (a == 999):
                return
            print a
            d2 = (d + action[a]) % len(forward)
            (dx,dy) = forward[d2]
            x2 = x + dx
            y2 = y + dy
            policy2D[x][y] = action_name[a]
            traverse(x2,y2,d2)

    traverse(init[0],init[1],init[2])

    for i in range(len(value)):
        print forward_name[i]
        for line in value[i]:
            for n in line:
                print "%4d" % n,
            print
        print

    for i in range(len(policy3D)):
        print forward_name[i]
        for line in policy3D[i]:
            for n in line:
                print "%4d" % n,
            print
        print

    for line in policy2D:
        print line
    return policy2D # Make sure your function returns the expected grid.


optimum_policy2D()

