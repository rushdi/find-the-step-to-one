# Moddasir Khan
# Find minimum steps to reach the destination number from 0

import sys
import numpy as np

sys.setrecursionlimit(10005)

noOfStepsArray = np.zeros((10001), dtype = np.int) 


# find minimum step to the target and return, (n -> 1) rather than (1 -> n)
def getSteps(n, memo): 

    # Minimum step for 1 is also 0
    if (n < 2):
        return 0;
        
    # memory initialize value is -1; if it is not -1 then already it has a value
    if (memo[n] != -1): 
        return memo[n] 
  
    # store the value for n as min(f(n-1), f(n//2), f(n//3)) - 1 
    noOfMinSteps = getSteps(n - 1, memo) 
    
    # even number
    if (n % 2 == 0): 
        noOfMinSteps = min(noOfMinSteps, getSteps(n // 2, memo)) 
        
    # odd number 
    if (n % 3 == 0): 
        noOfMinSteps = min(noOfMinSteps, getSteps(n - 1, memo)) 
  
    # save the result and return  
    memo[n] = 1 + noOfMinSteps 
    return memo[n] 

# initialize memory space based on current value
def initializeMemoForGetSteps(currentValue):
    # allocated the memory as array
    # initialize the array 
    memo = [0 for i in range(currentValue + 1)] 
    for i in range(currentValue + 1): 
        memo[i] = -1
                
    return (getSteps(currentValue, memo)) 

# initialize the loop and send the current value for the initialization of the memory
def initializeLoopWithRange(startInt, endInt):
    global noOfStepsArray
    for currentValue in range(startInt, endInt):
        noOfStepsArray[currentValue] = initializeMemoForGetSteps(currentValue)
        #print (currentValue, initializeMemoForGetSteps(currentValue))


