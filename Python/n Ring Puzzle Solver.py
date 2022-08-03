# Function called upon by the Ring Solving function to iterate the current ring state
def greySteps(i): 
	if (i == 1): return ["0", "1"]
	previous = greySteps(i - 1)
	updated, new = [], []
	for step in previous:
		updated.append("0" + step)
		new.append("1" + step)
	return updated + new[::-1]

# Recursive function to solve the rings
def solveRings(i):
    steps = greySteps(i)[::-1]
    for j in range(len(steps)):
        if steps[j] == "1"*i:
            return(steps[j:])
            
# Uses the piecewise function we found through our research to count the minimum 
# number of steps
def minSteps(i):
    if i % 2 == 0:
        return(1/3*(2**(i+1)-2))
    else:
        return(1/3*(2**(i+1)-1))

# ringCount = 3
# print("The steps to solve a "+ str(ringCount) + " ring puzzle are as follows:")
# print(solveRings(ringCount))
# print("The minimum number of steps required to solve a " + str(ringCount) + " ring puzzle is "+ str(int(minSteps(ringCount))) + " steps.")

ringCount = 9
print("The steps to solve a "+ str(ringCount) + " ring puzzle are as follows:")
print(solveRings(ringCount))
print("The minimum number of steps required to solve a " + str(ringCount) + " ring puzzle is "+ str(int(minSteps(ringCount))) + " steps.")

