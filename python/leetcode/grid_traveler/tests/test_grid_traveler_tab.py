import pytest
from ..grid_traveler_tab import GridTravelerTab
import numpy as np

class mocks:
	class one:
		m = 3
		n = 3
		unique_traversals = 6
	class three_two:
		m = 3
		n = 2
		unique_traversals = 3
	class eighteen:
		m = 18
		n = 18
		unique_traversals = 2333606220

class TestCanSum:
	@classmethod
	def setup_method(cls):
		cls.subject = GridTravelerTab()

	def assert_traversals_for(self, mock):
		assert mock.unique_traversals == self.subject.uniqueTraversals(
			mock.m,
			mock.n
		)

	def test_one(self):
		self.assert_traversals_for(mocks.one)

	def test_three_two(self):
		self.assert_traversals_for(mocks.three_two)

	def test_eighteen(self):
		self.assert_traversals_for(mocks.eighteen)

	@classmethod
	def teardown_class(cls):
		pass

# @pytest.mark.skip()