from unittest import TestCase
from ..is_palindrome import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.subject = Solution()

    def test_is_palindrome_negative_1(self):
        assert not self.subject.isPalindrome(-1)

    def test_is_palindrome_1(self):
        assert self.subject.isPalindrome(1)

    def test_is_palindrome_21(self):
        assert not self.subject.isPalindrome(21)

    def test_is_palindrome_11(self):
        assert self.subject.isPalindrome(11)

    def test_is_palindrome_123321(self):
        assert self.subject.isPalindrome(123321)

    def test_is_palindrome_12321(self):
        assert self.subject.isPalindrome(12321)

    def test_is_palindrome_12345(self):
        assert not self.subject.isPalindrome(12345)
