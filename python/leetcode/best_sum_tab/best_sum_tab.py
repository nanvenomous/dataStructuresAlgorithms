import numpy as np

class BestSumTab:
	def __init__(self): pass

	def bestSum(self, numbers, target):
		M = target + 1
		self.tab = [None for _ in range(M)]
		self.tab[0] = []
		for m in range(M):
			val = self.tab[m]
			if val == [] or val:
				for n in numbers:
					i = m + n
					if i <= target:
						curVal = self.tab[i]
						if not curVal:
							self.tab[i] = val + [n]
						else: self.tab[i] = min([curVal, val + [n]], key=len)
		return self.tab[-1]