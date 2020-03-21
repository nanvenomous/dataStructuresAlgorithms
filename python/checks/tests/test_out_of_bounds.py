import pytest
# from mock import patch
from ..out_of_bounds import insideInterval

class TestOutOfBounds:
	def test_checks_inside_bounds(self):
		assert insideInterval(25, (0, 50))

	def test_checks_out_of_bounds(self):
		assert not insideInterval(55, (0, 50))
		assert not insideInterval(-3, (0, 50))

	def test_checks_includes_edges_by_default(self):
		assert insideInterval(0, (0, 50))
		assert insideInterval(50, (0, 50))

	def test_checks_does_not_include_edges_on_request (self):
		assert not insideInterval(0, (0, 50), includeEdges=False)
		assert not insideInterval(50, (0, 50), includeEdges=False)