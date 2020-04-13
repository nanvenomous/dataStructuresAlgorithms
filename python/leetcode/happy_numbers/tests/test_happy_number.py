import pytest
from ..happy_number import HappyNumber, HappyNumberOptimize

class TestHappyNumber:

	@classmethod
	def setup_method(cls):
		cls.subject = HappyNumberOptimize()

	def test_identifies_happy_number(self):
		assert True == self.subject.isHappy(19)

	def test_identifies_unhappy_number(self):
		assert False == self.subject.isHappy(15)

class TestLoopRepeatsOnce:

	@classmethod
	def setup_method(cls):
		cls.subject = HappyNumber()
		cls.subject.possible_repeat = False
		cls.subject.history = []
		cls.subject.i1 = 0
		cls.subject.i2 = 0

	def test_finds_repeat(self):
		mock_squares = [5, 7, 6, 3, 2, 6, 3, 2, 6]
		for (i, num) in enumerate(mock_squares):
			self.subject.history.append(num)
			if i == len(mock_squares) - 1: assert True == self.subject.loop_repeats_once()
			else: assert False == self.subject.loop_repeats_once()
			if i <= 4: assert self.subject.possible_repeat == False
			else: assert self.subject.possible_repeat == True

	def test_resets_repeat(self):
		mock_squares = [5, 7, 6, 3, 2, 6, 3, 4]
		for (i, num) in enumerate(mock_squares):
			self.subject.history.append(num)
			assert False == self.subject.loop_repeats_once()
			if i <= 4: assert self.subject.possible_repeat == False
			elif i <= 6: assert self.subject.possible_repeat == True
			else: assert self.subject.possible_repeat == False

class TestAddSquaredDigits:

	@classmethod
	def setup_method(cls):
		cls.subject = HappyNumber()

	def test_squares_all_digits_and_sums(self):
		self.subject.cur = 324
		self.subject.add_squared_digits()
		assert self.subject.next == 3**2 + 2**2 + 4**2
		assert self.subject.cur == 0

	def test_squares_all_digits_with_many_zeros_and_sums(self):
		self.subject.cur = 1000
		self.subject.add_squared_digits()
		assert self.subject.next == 1
		assert self.subject.cur == 0