import pytest
from ..bit_manipulation import Bit

class TestIsNBitSet:

    @classmethod
    def setup_class(cls):
        cls.eight = Bit(8)

    def test_4th_bit_of_8_is_not_set(self):
        assert False == self.eight.is_set(4)

    def test_3rd_bit_of_8_is_set(self):
        assert True == self.eight.is_set(3)

    def test_2nd_bit_of_8_is_not_set(self):
        assert False == self.eight.is_set(2)

    def test_20th_bit_of_8_is_not_set(self):
        assert False == self.eight.is_set(20)

class TestBitManipulation:

    def assert_left_shift_equal(self, i, num):
        assert num << i == num*2**i

    def test_left_shift_same_as_multiply_by_2_raised_to_the_i_power(self):
        self.assert_left_shift_equal(2, 27)
        self.assert_left_shift_equal(6, 7)

    def assert_right_shift_equal(self, i, num):
        assert num >> i == int(num/2**i)

    def test_right_shift_same_as_divide_by_2_raised_to_the_i_power(self):
        self.assert_right_shift_equal(2, 27)
        self.assert_right_shift_equal(6, 7)

# @pytest.mark.skip()