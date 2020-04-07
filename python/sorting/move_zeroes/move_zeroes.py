from queue import Queue
from typing import List

class Solution(object):
    def moveZeroes(self, nums):
        # best solution from leetcode
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

class MoveZeroes:

    def __init__(self):
        super().__init__()
        self.nums = []
        self.num_i = Queue()
        self.zero_i = Queue()

    def moveZeroes(self, nums: List[int]) -> None:
        self.nums = nums
        self.num_i.queue.clear()
        self.zero_i.queue.clear()

        self._get_indices()
        self._reorder()

    def _get_indices(self):
        for (i, num) in enumerate(self.nums):
            if num == 0: self.zero_i.put(i)
            else: self.num_i.put(i)

    def _reorder(self):
        new_order = []
        while not self.num_i.empty():
            new_order.append(self.num_i.get())
        while not self.zero_i.empty():
            new_order.append(self.zero_i.get())
        self.nums[:] = [self.nums[i] for i in new_order]

class MoveZeroesStillTooSlow:

    def __init__(self):
        super().__init__()
        self.nums = []
        self.num_i = Queue()
        self.zero_i = Queue()
        self.ni = 0
        self.zi = 0
        self.zn = 0

    def moveZeroes(self, nums: List[int]) -> None:
        self.nums = nums
        self.num_i.queue.clear()
        self.zero_i.queue.clear()
        self.ni = 0
        self.zi = 0
        self.zn = 0

        self._get_indices()
        self._reorder()

    def _swap_positions(self):
        self.nums[self.zi] = self.nums[self.ni]
        self.nums[self.ni] = 0

    def _get_indices(self):
        for (i, num) in enumerate(self.nums):
            if num == 0: self.zero_i.put(i)
            else: self.num_i.put(i)

    def _swap_conditionally(self):
        if self.zi < self.ni:
            self._swap_positions()
            temp_i = self.zi
            self.zi = self.ni
            self.ni = temp_i
            if self.zn < self.ni:
                self.num_i.put(self.ni)

    def _swap_all_conditionally(self):
        self.num_i.put(None)
        for self.ni in iter(self.num_i.get, None):
            self._swap_conditionally()

    def _reorder(self):
        if self.zero_i.empty(): return
        else: self.zi = self.zero_i.get()
        while not self.zero_i.empty():
            self.zn = self.zero_i.get()
            self._swap_all_conditionally()
            self.zi = self.zn
        self._swap_all_conditionally()

class MoveZeroesTooSlow:

    def moveZeroes(self, nums: List[int]) -> None:
        self.nums = nums
        self.num_i = Queue()
        self.zero_i = Queue()

        self._get_indices()
        self._reorder()

    def _swap_positions(self, ni, zi):
        self.nums[zi] = self.nums[ni]
        self.nums[ni] = 0

    def _get_indices(self):
        for (i, num) in enumerate(self.nums):
            if num == 0: self.zero_i.put(i)
            else: self.num_i.put(i)

    def _reorder(self):
        while not self.zero_i.empty():
            zi = self.zero_i.get()
            self.num_i.put(None)
            for ni in iter(self.num_i.get, None):
                if zi < ni:
                    self._swap_positions(ni, zi)
                    zi = ni
                self.num_i.put(ni)

class MoveZeroesUnorderedNumbers:

    def moveZeroes(self, nums: List[int]) -> None:
        self.nums = nums
        self.ins = Queue()
        self.izs = Queue()
        i = len(nums) - 1

        while i >= 0:
            num = nums[i]
            if num == 0: self.izs.put(i)
            else: self.ins.put(i)
            i -= 1
        self.do_the_swaps()

    def do_the_swaps(self):
        inx = 0
        izx = 0
        self.izs.put(None)
        for zget in iter(self.izs.get, None):
            inx = self.ins.get()
            self.nums[zget] = self.nums[inx]
            self.nums[inx] = 0
