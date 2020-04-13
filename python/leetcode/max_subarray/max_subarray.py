from typing import List
import numpy as np
from threading import Thread
from queue import Queue

class MaxSubarray:
	def maxSubArray(self, nums: List[int]) -> int:
		curMax = nums[0]
		totMax = nums[0]
		i = 1
		while i < len(nums):
			num = nums[i]
			curMax = max(num, num + curMax)
			totMax = max(curMax, totMax)
			i += 1
		return totMax

class MaxSubarrayMath:

	def __init__(self):
		self.nums = None
		self.sub_sums = None

	def _get_max_right_to_left(self, s: int, e: int) -> int:
		sum = 0
		summed_values = []
		i = s
		while i >= e:
			num = self.nums[i]
			sum += num
			summed_values.insert(0, sum)
			i -= 1
		return e + np.argmax(summed_values)

	def _get_max_left_to_right(self, q: Queue, s: int, e: int):
		sum = 0
		summed_values = []
		i = s
		while i <= e:
			num = self.nums[i]
			sum += num
			summed_values.append(sum)
			i += 1
		q.put(s + np.argmax(summed_values))

	def multi_get_maxes(self, beginning: int, end: int):
		q = Queue()
		th = Thread(target=self._get_max_left_to_right, args=(q, beginning, end))
		th.start()
		i_max_left = self._get_max_right_to_left(end, beginning)
		th.join()
		i_max_right = q.get()
		print('## checking indices')
		print(i_max_left, i_max_right)
		if i_max_left == end and i_max_right == beginning:
			self.multi_get_maxes(beginning + 1, end - 1)
		elif i_max_left < i_max_right:
			self.sub_sums.append(sum(self.nums[i_max_left:i_max_right + 1]))
		elif i_max_left == i_max_right: self.sub_sums.append(self.nums[i_max_left])
		else:
			th = Thread(target=self.multi_get_maxes, args=(i_max_left, end))
			th.start()
			self.multi_get_maxes(beginning, i_max_right)
			th.join()

	def maxSubArray(self, nums: List[int]) -> int:
		self.nums = nums
		self.sub_sums = []
		beginning = 0
		end = len(self.nums) - 1
		self.multi_get_maxes(beginning, end)
		return max(self.sub_sums)