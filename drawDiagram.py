# Moddasir Khan
# Find minimum steps to reach the destination number from 0

import matplotlib.pyplot as plt

def drawResultAndExeTimeDiagram(noOfStepsArray, threadExeTime):
	#draw the result in a line diagram
	plt.figure("Result")
	plt.plot(noOfStepsArray, linestyle = 'dotted', marker = 'o')
	plt.title("No of Steps") 
	plt.xlabel('N')  
	plt.ylabel('Steps')

	#draw the execution time by thread in a line diagram
	plt.figure("Execution-Time")
	plt.plot(threadExeTime)
	plt.title("Execution Time by Thread") 
	plt.xlabel('Threads')  
	plt.ylabel('Time')  
	plt.show()