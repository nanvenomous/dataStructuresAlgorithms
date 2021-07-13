import numpy as np

class BestSumTab:
	def __init__(self): pass

	def bestSum(self, numbers, target):
		M = target + 1
		self.tab = [[] for _ in range(M)]
		self.tab[0].append([])
		for m in range(M):
			for li in self.tab[m]:
				for n in numbers:
					i = m + n
					if i <= target:
						self.tab[i].append(li + [n])
		return min(self.tab[-1], key=len)