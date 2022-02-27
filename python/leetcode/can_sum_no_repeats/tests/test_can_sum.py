import pytest
from ..can_sum import CanSum
import numpy as np

'''
[3, 4, 6, 2]

self: 3
allPrevious []
tabulation: [] + []

self :4
allPrevious: [(4 + 3)]
tabulation: [] + [7]

self: 6
allPrevious: [(6 + 4), (6 + 3)]
tabulation: [13] + [10, 9]

self: 2
allPrevious: [(2 + 6), (2 + 4), (2 + 3)]
tabulation: [15, 12, 11] + [8, 6, 5]

3, 4, 7, 6, 10, 9, 13, 2, 8, 6, 5, 12, 11, 15
'''

class mocks:
	class one:
		numbers = [3, 4, 6, 2]
		target = 9
		expected = [ 3.,  4.,  7.,  6.,  9., 10., 13.,  2.,  5.,  6.,  8., 11., 12., 15.,]

class TestCanSum:
	@classmethod
	def setup_method(cls):
		cls.subject = CanSum()

	def test_one(self):
		actual = self.subject.canSum(mocks.one.numbers, mocks.one.target)
		assert np.array_equal(actual, mocks.one.expected)

	@classmethod
	def teardown_class(cls):
		pass

# @pytest.mark.skip()