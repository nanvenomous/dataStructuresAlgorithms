import pytest
import random
# for output
# pytest -vs
# for no output
# pytest -v

from ..single_number import SingleNumberBruteSpace, SingleNumberHashTable

mock_list = [1, 2, 4, 1, 2]

class TestSingleNumberHashTable:
	@classmethod
	def setup_method(cls):
		cls.subject = SingleNumberHashTable()

	def test_returns_simple_single_number(self):
		assert 1 == self.subject.singleNumber([1])

	def test_randomized_returns_simple_single_number(self):
		print()
		for _ in range(100):
			random.shuffle(mock_list)
			print(mock_list)
			assert 4 == self.subject.singleNumber(mock_list)

@pytest.mark.skip()
class TestSingleNumber:
	@classmethod
	def setup_method(cls):
		cls.subject = SingleNumberBruteSpace()

	def test_returns_simple_single_number(self):
		assert 1 == self.subject.singleNumber([1])

	def test_randomized_returns_simple_single_number(self):
		print()
		subj = SingleNumberBruteSpace()
		for _ in range(100):
			random.shuffle(mock_list)
			print(mock_list)
			subj.singleNumber(mock_list)
			assert [4] == subj.seen

@pytest.mark.skip()
class TestConfirmRemove:
	@classmethod
	def setup_method(cls):
		cls.subject = SingleNumberBruteSpace(seen=[1, 3, 2])

	def test_removes_from_beginning(self):
		self.subject.num = 1
		self.subject.confirm_remove()
		assert [3, 2] == self.subject.seen

	def test_removes_from_end(self):
		self.subject.num = 2
		self.subject.confirm_remove()
		assert [1, 3] == self.subject.seen

	def test_does_not_remove_and_appends(self):
		self.subject.num = 4
		self.subject.confirm_remove()
		assert [1, 3, 2, 4] == self.subject.seen

	def test_appends_first(self):
		self.subject.num = 4
		self.subject.seen = []
		self.subject.confirm_remove()
		assert [4] == self.subject.seen
