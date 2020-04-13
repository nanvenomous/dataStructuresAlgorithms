from ..SinglyLinkedList import SinglyLinkedList

mock_linked_list = SinglyLinkedList([8, 0, 7])

class TestSinglyLinkedList:
	def test_properly_references_head(self):
		assert mock_linked_list.head.val == 7

	def test_properly_references_second_element(self):
		assert mock_linked_list.head.next.val == 0

	def test_properly_references_tail(self):
		assert mock_linked_list.tail.val == 8

	def test_gets_printable_list(self):
		assert ['7', '0', '8'] == SinglyLinkedList._get_printable(mock_linked_list.head)
