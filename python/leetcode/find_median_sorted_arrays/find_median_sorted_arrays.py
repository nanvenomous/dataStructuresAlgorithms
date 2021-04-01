from typing import List
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class FindMedianSortedArray:
    def __init__(self) -> None:
        pass

    def _getOddMid(self, joint):
        return int(((len(joint) - 2) / 2)) + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joint = nums1 + nums2
        joint.sort()
        if len(joint) % 2 == 0: # do even
            leftMid = int((len(joint)-1) / 2)
            rightMid = leftMid + 1
            print(leftMid)
            print(joint)
            print(joint[leftMid], joint[rightMid])
            return (joint[leftMid] + joint[rightMid])/2
        else: # do odd
            return joint[self._getOddMid(joint)]