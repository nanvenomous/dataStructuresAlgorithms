import pytest
from ..grid_traveler_tab import GridTravelerTab
import numpy as np

class mocks:
	class one:
		m = 3
		n = 3
		unique_traversals = 6

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

	@classmethod
	def teardown_class(cls):
		pass

# @pytest.mark.skip()