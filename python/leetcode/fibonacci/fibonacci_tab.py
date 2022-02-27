import numpy as np

class FibonacciTab:
	def __init__(self):
		self.seq = None

	def fibNumberAt(self, n):
		self.seq = np.zeros(n + 1)
		self.seq[1] = 1
		for i in range(2, n + 1):
			self.seq[i] = self.seq[i - 1] + self.seq[i - 2]
		return self.seq[n]
