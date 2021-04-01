import pytest
from unittest.mock import patch
from ..find_median_sorted_arrays import FindMedianSortedArray

class mocks:
    class one: 
        nums1 = [1,2]
        nums2 = [3,4]
    class two:
        nums1 = [1,3]
        nums2 = [2]
    class three:
        nums1 = [0,0]
        nums2 = [0,0]
    class four:
        nums1 = []
        nums2 = [1]

class answers:
    one = 2.50000
    two = 2.00000
    three = 0.00000
    four = 1.00000

class TestFindMedianSortedArray:
    @classmethod
    def setup_method(cls):
        cls.subject = FindMedianSortedArray()

    def assert_gets_median_of_arrays(self, mock, ans):
        assert self.subject.findMedianSortedArrays(mock.nums1, mock.nums2) == ans

    def test_mock_one(self):
        self.assert_gets_median_of_arrays(mocks.one, answers.one)

    def test_mock_two(self):
        self.assert_gets_median_of_arrays(mocks.two, answers.two)

    def test_mock_three(self):
        self.assert_gets_median_of_arrays(mocks.three, answers.three)

    def test_mock_four(self):
        self.assert_gets_median_of_arrays(mocks.four, answers.four)

    @classmethod
    def teardown_class(cls): pass

# @pytest.mark.skip()