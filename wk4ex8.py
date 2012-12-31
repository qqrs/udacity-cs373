# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

#grid = [[0, 0, 1, 0, 0, 0],
        #[0, 0, 1, 0, 0, 0],
        #[0, 0, 0, 0, 1, 0],
        #[0, 0, 1, 1, 1, 0],
        #[0, 0, 0, 0, 1, 0]]

grid = [[0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

#def in_bounds(y,x):
    #return (x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid))

#def cell_unseen(y,x):
    #for it in openlist:
        #if (y == it[1] and x == it[2]):
            #return False

    #for it in expanded:
        #if (y == it[1] and x == it[2]):
            #return False

    #return True


def search():
    openlist = list()
    expanded = list()
    openlist.append([0, init[0], init[1]])
    while len(openlist) > 0:
        c = openlist[0]
        for d in delta:
            y = c[1] + d[0]
            x = c[2] + d[1]

            if (not (x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid))):
                continue
            if (grid[y][x] != 0):
                continue
            if (y == goal[0] and x == goal[1]):
                return ([c[0]+cost,y,x])

            found = False
            for it in openlist:
                if (y == it[1] and x == it[2]):
                    found = True
                    break

            if (found):
                continue

            for it in expanded:
                if (y == it[1] and x == it[2]):
                    found = True
                    break

            if (found == True):
               continue

            openlist.append([c[0]+cost,y,x])

        expanded.append(c)
        del openlist[0]
        openlist.sort(key=lambda op: op[0])
    return 'fail'



    # initialize open list
    # while open list not empty
    #   expand item from open list with smallest path length
    #       for each direction delta in bounds and not blocked
    #          add new grid to open list (or update if already in list?)
    #   sort open list
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

print search()



