# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

#success_prob = 0.5                      
success_prob = 1.0                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    def compute_value_recurse(x, y, cost, dname):
        value[x][y] = cost
        policy[x][y] = dname
        adjacent_cost = list()
        for (dx,dy) in delta:
            (x2,y2) = (x + dx, y + dy)
            if (x2 in range(len(grid)) and y2 in range(len(grid[0]))
                    and grid[x2][y2] != 1):
                adjacent_cost.append(value[x2][y2])
            else:
                adjacent_cost.append(collision_cost)

        print "(%4d,%4d)" % (x,y),
        for c in adjacent_cost:
            print "%9.2f" % c,
        print 
        for line in value:
            for n in line:
                print "%9.2f" % n,
            print 
        for a in range(len(delta)):
            (dx,dy) = delta[a]
            (x2,y2) = (x - dx, y - dy)
            if (x2 in range(len(grid)) and y2 in range(len(grid[0]))):
                exp_value = (cost_step + 
                             success_prob * adjacent_cost[a] +
                             failure_prob * adjacent_cost[(a-1) % len(delta)] +
                             failure_prob * adjacent_cost[(a+1) % len(delta)] )
                if (grid[x2][y2] != 1 and value[x2][y2] > exp_value):
                    compute_value_recurse(x2,y2,exp_value,delta_name[a])

    compute_value_recurse(goal[0], goal[1], 0.0, '*')

    print
    for line in value:
        for n in line:
            print "%9.2f" % n,
        print 
    for line in policy:
        print line
    return value, policy

stochastic_value()



