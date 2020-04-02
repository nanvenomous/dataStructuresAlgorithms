from typing import List

class SingleNumberBruteIter:
	def singleNumber(self, nums: List[int]) -> int:
		for (j, num) in enumerate(nums):
			i = j + 1
			while num != nums[i]:
				if i == len(nums) - 1: return num
				i += 1

class SingleNumberBruteSpace:
	def __init__(self, seen=[]):
		self.seen = seen
		self.num = None

	def confirm_remove(self):
		for (i, elem) in enumerate(self.seen):
			if self.num == elem:
				del self.seen[i]
				return
		self.seen.append(self.num)

	def singleNumber(self, nums: List[int]) -> int:
		self.num = None
		self.seen = []
		j = 0
		while j < len(nums):
			self.num = nums[j]
			self.confirm_remove()
			j += 1
		return self.seen[0]