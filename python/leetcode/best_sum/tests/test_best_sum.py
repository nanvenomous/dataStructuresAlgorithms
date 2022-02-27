import pytest
from ..best_sum import BestSum
import numpy as np

class mocks:
	class one:
		numbers = [3, 6, 2]
		target = 8
		expected = [2, 6]
	class two:
		numbers = [5, 3, 4, 7]
		target = 7
		expected = [7]
	class three:
		numbers = [2, 3, 5]
		target = 8
		expected = [5, 3]

class TestBestSum:
	@classmethod
	def setup_method(cls):
		cls.subject = BestSum()

	def assert_best_sum_for_mock(self, mock):
		actual = self.subject.bestSum(mock.numbers, mock.target)
		assert mock.expected == actual

	def test_one(self):
		self.assert_best_sum_for_mock(mocks.one)

	def test_two(self):
		self.assert_best_sum_for_mock(mocks.two)

	def test_three(self):
		self.assert_best_sum_for_mock(mocks.three)

	@classmethod
	def teardown_class(cls):
		pass

# @pytest.mark.skip()