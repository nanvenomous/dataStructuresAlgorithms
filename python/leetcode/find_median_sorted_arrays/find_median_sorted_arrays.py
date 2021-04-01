from typing import List
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# [2, 5, 12]
# [1, 6, 7, 9, 22]

class FindMedianSortedArray:
    def __init__(self) -> None:
        pass

    def _getMid(self, joint):
        return int((len(joint)- 1)/2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joint = nums1 + nums2
        joint.sort()
        if len(joint) % 2 == 0: # do even
            leftMid = self._getMid(joint)
            rightMid = leftMid + 1
            return (joint[leftMid] + joint[rightMid])/2
        else: # do odd
            return joint[self._getMid(joint)]