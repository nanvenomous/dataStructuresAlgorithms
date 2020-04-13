# Definition for singly-linked list.

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class SinglyLinkedList:

	def __init__(self, nodes_list):
		def nex_list_node():
			return ListNode(nodes_list.pop())
		self.head = nex_list_node()
		self.tail = self.head
		while (nodes_list):
			self.tail.next = nex_list_node()
			self.tail = self.tail.next

	@staticmethod
	def _get_printable(listNode):
		printable = []
		def add_to_printable(to_add): printable.append(str(to_add))
		add_to_printable(listNode.val)
		while (listNode.next):
			add_to_printable(listNode.next.val)
			listNode = listNode.next
		return printable

	@classmethod
	def print(cls, listNode):
		if type(listNode) != ListNode:
			raise TypeError('argument must be ListNode')
		printable = cls._get_printable(listNode)
		print(' -> '.join(printable))