import pytest
from ..longest_consecutive import LongestConsecutive
from ..longest_consecutive import Node

# 1 -> 3 -> 4
#  \
#   6
# return 2

# 1 -> 3 -> 4
#  \
#   2 -> 8 -> 9 -> 10
#    \
#     3 -> 4
# return 4

class mocks:
    simplest = Node(1, [
        Node(3, [
            Node(4)
        ]),
        Node(6)
    ])
    ex2 = Node(1, [
        Node(3, [Node(4)]),
        Node(2, [
            Node(8, [Node(9, [Node(10)])]),
            Node(3, [Node(4)])
            ]),
    ])

class TestLongestConsecutive:
    @classmethod
    def setup_method(cls):
        cls.subject = LongestConsecutive()

    def test_ex2(self):
        ans = self.subject.getLongestConsecutive(mocks.ex2)
        assert 4 == ans

    def test_simplest(self):
        ans = self.subject.getLongestConsecutive(mocks.simplest)
        assert 2 == ans

# @pytest.mark.skip()