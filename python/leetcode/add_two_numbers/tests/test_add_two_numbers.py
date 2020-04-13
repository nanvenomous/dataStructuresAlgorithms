import pytest
from ..add_two_numbers import Solution
from ..SinglyLinkedList import SinglyLinkedList, ListNode

def _get_list_head(lst):
	lnkLst = SinglyLinkedList(lst)
	return lnkLst.head

mock_708 = _get_list_head([8, 0, 7])
mock_243 = _get_list_head([3, 4, 2])
mock_564 = _get_list_head([4, 6, 5])

mock_24 = _get_list_head([4, 2])
mock_7 = _get_list_head([7])
mock_31 = _get_list_head([1, 3])

mock_3 = _get_list_head([3])
mock_10 = _get_list_head([0, 1])

mock_1 = _get_list_head([1])
mock_99 = _get_list_head([9, 9])
mock_100 = _get_list_head([0, 0, 1])

class TestAddTwoNumbers:
	@classmethod
	def setup_class(cls):
		cls.subject = Solution()

	def test_splits_numbers(self):
		one, two = self.subject._split(17)
		assert (1, 7) == (one, two)

	def test_splits_single_number(self):
		one, two = self.subject._split(8)
		assert (0, 8) == (one, two)

	def test_splits_ten(self):
		one, two = self.subject._split(10)
		assert (1, 0) == (one, two)

	def test_split_errors_if_passed_in_string(self):
		with pytest.raises(TypeError):
			self.subject._split('')

	def test_split_errors_if_passed_in_ListNode(self):
		with pytest.raises(TypeError):
			self.subject._split(ListNode(2))

	def test_returns_zero_when_given_none(self):
		assert 0 == self.subject._otherwise_zero(None)

	def test_returns_number_when_ListNode_with_that_val(self):
		assert 12 == self.subject._otherwise_zero(ListNode(12))

	def test_next_or_none_returns_none_if_none(self):
		assert None == self.subject._next_or_none(None)

	def test_next_or_none_returns_none_if_ListNode_desnt_have_next(self):
		assert None == self.subject._next_or_none(ListNode(12))

	def test_next_or_none_returns_ListNode_if_ListNode_has_next(self):
		assert mock_243.next == self.subject._next_or_none(mock_243)

	def test_at_least_one_next_returns_false_if_next_none_and_current_none(self):
		assert False == self.subject._at_least_one_next(ListNode(12), None)

	def test_at_least_one_next_returns_false_if_both_none(self):
		assert False == self.subject._at_least_one_next(None, None)

	def test_at_least_one_next_returns_true_if_both_next(self):
		assert True == self.subject._at_least_one_next(mock_243, mock_564)

	@classmethod
	def linked_lists_equal(cls, l1, l2, equal=True):
		if l1.val == l2.val: equal = equal & True
		if not all((l1.next, l2.next)):
			if not any((l1.next, l2.next)):
				return equal
			else: return False
		return cls.linked_lists_equal(l1.next, l2.next, equal)

	def test_adds_two_linked_list_numbers(self):
		sum_attempt = self.subject.addTwoNumbers(mock_243, mock_564)
		print()
		SinglyLinkedList.print(sum_attempt)
		SinglyLinkedList.print(mock_708)
		assert self.linked_lists_equal(mock_708, sum_attempt)

	def test_adds_two_linked_list_numbers_of_different_sizes(self):
		sum_attempt = self.subject.addTwoNumbers(mock_24, mock_7)
		print()
		SinglyLinkedList.print(sum_attempt)
		SinglyLinkedList.print(mock_31)
		assert self.linked_lists_equal(mock_31, sum_attempt)

	def test_adds_two_linked_list_numbers_with_none_next_but_carry(self):
		sum_attempt = self.subject.addTwoNumbers(mock_3, mock_7)
		print()
		SinglyLinkedList.print(sum_attempt)
		SinglyLinkedList.print(mock_10)
		assert self.linked_lists_equal(mock_10, sum_attempt)

	def test_adds_two_linked_list_numbers_with_double_carryover(self):
		sum_attempt = self.subject.addTwoNumbers(mock_1, mock_99)
		print()
		SinglyLinkedList.print(sum_attempt)
		SinglyLinkedList.print(mock_100)
		assert self.linked_lists_equal(mock_100, sum_attempt)