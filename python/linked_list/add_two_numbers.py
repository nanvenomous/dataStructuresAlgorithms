from .SinglyLinkedList import ListNode

class Solution:
    @staticmethod
    def _split(sum):
        firstNum = int(sum/10)
        secondNum = sum % 10
        return firstNum, secondNum

    @staticmethod
    def _otherwise_zero(node): return node.val if node else 0

    @staticmethod
    def _next_or_none(node): return node.next if node else None

    @classmethod
    def _at_least_one_next(cls, val1, val2):
        next = (cls._next_or_none(val1), cls._next_or_none(val2))
        return any(next)

    def addTwoNumbers(self, l1, l2, carried=0):
        sum = self._otherwise_zero(l1) + self._otherwise_zero(l2) + carried
        toCarry, thisNum = self._split(sum)
        listNode = ListNode(thisNum)
        print(sum, toCarry)
        if self._at_least_one_next(l1, l2) or toCarry > 0:
            listNode.next = self.addTwoNumbers(
                self._next_or_none(l1),
                self._next_or_none(l2),
                toCarry
                )
        return listNode
