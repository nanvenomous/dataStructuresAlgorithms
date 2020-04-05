import pytest
from ..max_subarray import MaxSubarray

mock_rollercoaster = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
mock_valley = [2, -3, 1, 15, -1, -25, 9, -5, 6]

class TestMaxSubarray:

	@classmethod
	def setup_method(cls):
		cls.subject = MaxSubarray()

	def test_returns_correct_max_three_neg_input(self):
		print()
		assert self.subject.maxSubArray([-2,-1,-2]) == -1

	def test_returns_correct_max_pos_input_neg_input(self):
		print()
		assert self.subject.maxSubArray([1, -3]) == 1

	def test_returns_correct_max_two_pos_inputs(self):
		print()
		assert self.subject.maxSubArray([1, 2]) == 3

	def test_returns_correct_max_single_input(self):
		print()
		assert self.subject.maxSubArray([1]) == 1

	def test_returns_correct_max_rollercoaster(self):
		assert self.subject.maxSubArray(mock_rollercoaster) == 6

	def test_returns_correct_max_valley(self):
		assert self.subject.maxSubArray(mock_valley) == 16

	@pytest.mark.skip()
	def test_returns_correct_maxes_valley_former(self):
		self.subject.maxSubArray([2, -3, 1, 15])
		assert self.subject.sub_sums == [16]

	@pytest.mark.skip() # warning this test could fail because of multithreading
	def test_returns_correct_maxes_valley(self):
		self.subject.maxSubArray(mock_valley)
		assert self.subject.sub_sums == [10, 16]

	@pytest.mark.skip()
	def test_returns_correct_maxes_valley_latter(self):
		self.subject.sub_sums = []
		self.subject.nums = mock_valley
		self.subject.multi_get_maxes(6, 8)
		assert self.subject.sub_sums == [10]

@pytest.mark.skip()
class TestMaxSubarrayPlotting:

	@classmethod
	def setup_class(cls):
		import matplotlib.pyplot as plt
		cls.plt = plt

	@classmethod
	def setup_method(cls):
		cls.subject = MaxSubarray()

	@pytest.mark.skip()
	def test_plot_values(self):
		self.plt.figure()
		self.plt.title('rollercoaster values')
		self.plt.xlabel('index')
		self.plt.ylabel('value')
		self.plt.plot(range(0, len(mock_rollercoaster)), mock_rollercoaster)

	def plot_sum_left_to_right(self, name, data):
		sum = 0
		summed_values = []
		for num in data:
			sum += num
			summed_values.append(sum)

		sum = 0
		summed_values = []
		i = 0
		while i < len(data):
			num = data[i]
			sum += num
			summed_values.append(sum)
			i += 1

		self.plt.figure()
		self.plt.title(name + ': sum the array from left to right')
		self.plt.xlabel('index')
		self.plt.ylabel('sum value')
		self.plt.plot(range(0, len(data)), summed_values)

	def plot_sum_right_to_left(self, name, data):
		sum = 0
		summed_values = []
		i = len(data) - 1
		while i >= 0:
			num = data[i]
			sum += num
			summed_values.insert(0, sum)
			i -= 1

		self.plt.figure()
		self.plt.title(name + ': sum the array from right to left')
		self.plt.xlabel('index')
		self.plt.ylabel('sum value')
		self.plt.plot(range(0, len(data)), summed_values)

	@pytest.mark.skip()
	def test_plot_sums_rollercoaster(self):
		name = 'rollercoaster'
		data = mock_rollercoaster
		self.plot_sum_left_to_right(name, data)
		self.plot_sum_right_to_left(name, data)

	def test_plot_sums_valley(self):
		name = 'valley'
		data = mock_valley
		self.plot_sum_left_to_right(name, data)
		self.plot_sum_right_to_left(name, data)

	@classmethod
	def teardown_class(cls):
		cls.plt.show()
