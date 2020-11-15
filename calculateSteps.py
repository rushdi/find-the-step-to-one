# Moddasir Khan
# Find minimum steps to reach the destination number from 0

from threading import *
import sys

sys.setrecursionlimit(10005)

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
    for currentValue in range(startInt, endInt):
        print (currentValue, initializeMemoForGetSteps(currentValue))


def main():
    # start and end range
    startInt = 1
    endInt = 10000
    
    # split the range for the better calculation
    splitRange = endInt // 100
    # split range count for the thread counting
    splitRangeCount = 0
    
    # when splitRange bigger than the count of the range then the loop going to stop
    while (splitRange > splitRangeCount):
        # find start and end point for the loop range to calculate steps
        if (splitRangeCount == 0):
            endInt = splitRange
#             print(splitRange, splitRangeCount, startInt , endInt)
            splitRangeCount += 1
        else:
            startInt = startInt + splitRange
            splitRangeCount += 1
            endInt += splitRange
#             print(splitRange, splitRangeCount, startInt , endInt)
            
#         initializeLoopWithRange(startInt, endInt)
        # create a new thread
        t = Thread(target= initializeLoopWithRange(startInt, endInt))
        # set name of this thread
        t.setName("Thread " + str(splitRangeCount))
        # start the thread
        t.start()
        # make current thread to wait for thread t to complete
        t.join()
        # code executed in main thread
        print(t.getName() + " is completed")
        

if __name__ == "__main__":
    main()
