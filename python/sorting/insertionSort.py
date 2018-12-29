import numpy as np

def swap(index1, index2, array):
	array[index1], array[index2] = array[index2], array[index1]

def insertionSort(x, elem, index):
	# get index of current element to sort
	cIndex = index # changing this won't change index
	# index of already sorted element to check
	sIndex = index - 1 # sub index
	# iterate through already sorted list in reverese
	while sIndex >= 0:
		sElem = x[sIndex]
		# swap if our element is less than the current
		if (elem < sElem):
			swap(sIndex, cIndex, x)
		else:
			break # you found it's place in the sorted array
		# update indices after the swap (if loop continues)
		sIndex -= 1
		cIndex -= 1

def singleSort(x):
	index = 1
	while index < len(x): # iterate to the last elem
		# setup
		elem = x[index]
		# for each elem and index, insert current element into the sorted list
		insertionSort(x, elem, index)
		#increment for loop
		index += 1

x = np.array([2, 8, 5, 3, 9, 4])
print(x)
singleSort(x)
print(x)