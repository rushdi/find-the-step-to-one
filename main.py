# Moddasir Khan
# Find minimum steps to reach the destination number from 0

from threading import *
import matplotlib.pyplot as plt
import numpy as np
import time
import calculateSteps
import drawDiagram


def main():
    # start and end range
    startInt = 1
    endInt = 10000

    # split the range for the better calculation
    splitRange = endInt // 100
    # split range count for the thread counting
    splitRangeCount = 0

    threadExeTime = np.zeros((splitRange + 1), dtype = np.float) 
    
    # when splitRange bigger than the count of the range then the loop going to stop
    while (splitRange > splitRangeCount):
        # find start and end point for the loop range to calculate steps
        if (splitRangeCount == 0):
            endInt = splitRange
            splitRangeCount += 1
        else:
            startInt = startInt + splitRange
            splitRangeCount += 1
            endInt += splitRange
                     
        #initializeLoopWithRange(startInt, endInt)
        #mark the start time
        startTime = time.time()
        # create a new thread
        t = Thread(target= calculateSteps.initializeLoopWithRange(startInt, endInt + 1))
        # set name of this thread
        t.setName("Thread " + str(splitRangeCount))
        # start the thread
        t.start()
        # make current thread to wait for thread t to complete
        t.join()

        #mark the end time
        endTime = time.time()
        #calculate the total time it took to complete the thread
        workTime =  endTime - startTime
        #append work time in a list
        threadExeTime[splitRangeCount] = workTime

        #code executed in main thread
        print(t.getName() + " is completed")        

    #draw the result
    drawDiagram.drawResultAndExeTimeDiagram(calculateSteps.noOfStepsArray, threadExeTime)

        

if __name__ == "__main__":
    main()