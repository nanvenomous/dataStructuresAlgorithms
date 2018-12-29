import numpy as np

def swap(index1, index2, array):
	array[index1], array[index2] = array[index2], array[index1]

def singleSort(x):
	index = 1
	while index < (len(x) - 1): # iterate to the 2nd to last elem
		# setup
		elem = x[index]
		nextIndex = index + 1
		nextElem = x[nextIndex]
		# find place for swap
		for oElem in x[:index - 1].reversed():

		#increment for loop
		index += 1

x = np.array([2, 8, 5, 3, 9, 4])
print(x)
singleSort(x)
print(x)