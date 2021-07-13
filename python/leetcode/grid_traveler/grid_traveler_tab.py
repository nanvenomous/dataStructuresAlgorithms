import numpy as np

class GridTravelerTab:
	def __init__(self): pass

	def uniqueTraversals(self, m, n):
		x = m + 1; y = n + 1
		shape = (x, y)
		self.tab = np.zeros(shape)
		self.tab[1][1] = 1
		for xi in range(x):
			for yi in range(y):
				elem = self.tab[xi][yi]
				if (xi + 1) < x and yi < y:
					self.tab[xi + 1][yi] += elem
				if xi < x and (yi + 1) < y:
					self.tab[xi][yi + 1] += elem
		print()
		print(self.tab)
		return self.tab[-1][-1]