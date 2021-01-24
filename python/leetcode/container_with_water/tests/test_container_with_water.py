import pytest
from ..container_with_water import ContainerWithWater

class mocks:
    one = [1, 3, 3]
    two = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    bridge_outside = [1, 4, 1, 1, 27, 27, 1, 1, 4, 1]
    bridge_inside = [1, 4, 1, 1, 29, 29, 1, 1, 4, 1]
    false_peak = [1, 6, 7, 1, 9, 7, 1, 6, 1]

class TestContainerWithWater:
    @classmethod
    def setup_method(cls):
        cls.subject = ContainerWithWater()

    def test_solves_single_area(self):
        self.subject.heights = mocks.one
        self.subject.end = len(mocks.one)
        self.subject.singleArea()
        assert 3 == self.subject.maxArea

    def assert_max_area(self, mock, ans):
        self.subject.findArea(mock)
        assert self.subject.maxArea == ans

    def test_solves_for_biggest_area(self):
        self.assert_max_area(mocks.two, 49)

    def test_solves_bridge_outside(self):
        self.assert_max_area(mocks.bridge_outside, 28)

    def test_solves_bridge_inside(self):
        self.assert_max_area(mocks.bridge_inside, 29)

    def test_solves_false_peak(self):
        self.assert_max_area(mocks.false_peak, 36)

    @classmethod
    def teardown_class(cls): pass

# @pytest.mark.skip()