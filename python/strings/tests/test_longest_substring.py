import pytest
from ..longest_substring import Solution

mock_3 = 'abcabcbba'

class TestLongestSubstring:
	@classmethod
	def setup_class(cls):
		soln = Solution()
		cls.subject = soln.lengthOfLongestSubstring

	def test_splits_numbers(self):
		assert 3 == self.subject(mock_3)
