import numpy as np
from selectionSort import singleSort as selectionSort

def swap(index1, index2, array):
	array[index1], array[index2] = array[index2], array[index1]

def singleGapSwap(x, gap):
	# iterate through array at gap size
	i = 0
	endConsideringGap = (len(x) - gap) - 1 # extra -1 to get past the gap
	while (i < endConsideringGap):
		# setup loop
		lElem = x[i]
		rI = i + gap + 1
		rElem = x[rI]
		# if element on left is larger
		if (lElem > rElem):
			swap(i, rI, x) # then switch their positions
		i += 1 # continue to increment loop

def singleSort(x, gap):
	if (gap > len(x)):
		print('gap must be smaller than size of array')
		return
	# do shell sort
	while (gap > 0):
		singleGapSwap(x, gap)
		gap -= 1

x = np.array([14, 18, 19, 37, 23, 40, 29, 30, 11])
print('original array')
print(x)
print()

singleSort(x, 4)
print('shell sorted array')
print(x)
print()

selectionSort(x)
print('final array (after selection sort)')
print(x)