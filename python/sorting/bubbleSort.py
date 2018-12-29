# bubblesort has the following order
#	- O(n^2) worst case

import numpy as np

def swap(index1, index2, array):
	array[index1], array[index2] = array[index2], array[index1]

def singleSort(x):
	index = 0
	while index < (len(x) - 1): # iterate to the 2nd to last elem
		# setup
		elem = x[index]
		nextIndex = index + 1
		nextElem = x[nextIndex]
		# swap elements if unordered
		if (elem > nextElem):
			swap(index, nextIndex, x)
		index += 1
	# last element is now the greatest
	if (len(x) > 2): # if array is big enough
		# call on subset (minus the last element)
		singleSort(x[:-1])

x = np.array([2, 8, 5, 3, 9, 4, 1])
print(x)
singleSort(x)
print(x)