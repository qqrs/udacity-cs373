# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    def compute_value_recurse(x, y, cost):
        value[x][y] = cost
        for (dx,dy) in delta:
            x2 = x - dx
            y2 = y - dy
            if (x2 in range(len(grid)) and y2 in range(len(grid[0]))):
                if (grid[x2][y2] != 1 and value[x2][y2] > cost + cost_step):
                    compute_value_recurse(x2,y2,cost+cost_step)

    compute_value_recurse(goal[0], goal[1], 0)

    return value #make sure your function returns a grid of values as demonstrated in the previous video.


#for line in compute_value():
    #print line

