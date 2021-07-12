'''
[3, 4, 6, 2], 8

[2, 2, 2, 2]
[4, 2, 2]
[3, 3, 2]
[6, 2]

8 - 4 = 4
4 - 2 = 2
2 - 2 = 0
'''

class BestSum:
	def __init__(self): pass

	def bestSum(self, numbers, target):
		if target == 0: return []
		if target < 0: return None
		shortest = None
		for n in numbers: # find sub sums
			rem = target - n

			subSolution = self.bestSum(numbers, rem)
			if subSolution != None:
				nxtSolution = subSolution + [n]
				if (shortest == None) or (len(nxtSolution) < len(shortest)):
					shortest = nxtSolution
		return shortest

# m is size of target
# n is length of numbers
# normal time complexity is n^m