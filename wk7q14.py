import random

unfilled = 0
tests = 100000
for count in range(tests):
    grid = [0 for _ in range(4)]
    for i in range(12):
        x = (int)(4.0*random.random())
        grid[x] += 1
    if (grid[0] > 0):
    #if (grid[0] > 0 and grid[1] > 0 and grid[2] > 0 and grid[3] > 0):
        pass
    else:
        unfilled += 1
    
print unfilled
print tests
print (unfilled / float(tests))

