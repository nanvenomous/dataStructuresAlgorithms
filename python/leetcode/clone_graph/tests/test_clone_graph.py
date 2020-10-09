import pytest
from ..clone_graph import CloneGraph, Node

class TestCloneGraph:

	@classmethod
	def setup_method(cls):
		cls.subject = CloneGraph()

	def test_returns_correct_max_three_neg_input(self):
		self.subject.cloneGraph(None)

	@classmethod
	def teardown_class(cls): pass

# @pytest.mark.skip()