import pytest
from ..fibonacci_tab import FibonacciTab

class TestCanSum:
	@classmethod
	def setup_method(cls):
		cls.subject = FibonacciTab()

	def test_eight(self):
		assert 21 == self.subject.fibNumberAt(8)

	def test_fifty(self):
		assert 12586269025 == self.subject.fibNumberAt(50)

	@classmethod
	def teardown_class(cls):
		pass

# @pytest.mark.skip()