import numpy as np

def swap(index1, index2, array):
	array[index1], array[index2] = array[index2], array[index1]

def getMinimumIndex(subX):
	indexMin = 0
	minimum = subX[0]
	index = 1
	while index < len(subX):
		elem = subX[index]
		if (elem < minimum):
			minimum = elem
			indexMin = index
		index += 1
	return indexMin

def singleSort(x):
	index = 0
	while index < (len(x) - 1): # iterate to the 2nd to last elem
		subIndexMin = getMinimumIndex(x[index:])
		indexMin = subIndexMin + index
		swap(indexMin, index, x)
		index += 1

x = np.array([11, 16, 2, 8, 1, 9, 4, 7])
# print(x)
singleSort(x)
# print(x)