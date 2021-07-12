import numpy as np

class CanSum:
	def __init__(self):
		self.solution = np.array([])
		pass

	def canSum(self, numbers, target):
		numbers = np.array(numbers)
		tabulation = np.array([])
		for i, n in enumerate(numbers):
			# add self
			self.solution = np.append(self.solution, n)
			# get self + all previous
			allPrevious = n + np.array(numbers[0:i])
			# add self + tabulation
			tabulation += n
			tabulation = np.concatenate((allPrevious, tabulation))
			self.solution = np.concatenate((self.solution, tabulation))
		return self.solution
