from typing import List
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# [2, 5, 12]
# [1, 6, 7, 9, 22]

class FindMedianSortedArray:
    def __init__(self) -> None:
        pass

    def _getMid(self, joint):
        return int((len(joint)- 1)/2)

    def _combineSort(self, nums1, nums2):
        joint = []
        i1 = 0
        i2 = 0
        while True:
            if i2 < len(nums2):
                num2 = nums2[i2]
                if i1 < len(nums1):
                    num1 = nums1[i1]
                    # add the smaller of the two
                    if num1 < num2:
                        joint.append(num1)
                        i1 += 1
                    else:
                        joint.append(num2)
                        i2 += 1
                else: # handle add rest of nums2 & break
                    joint += nums2[i2:len(nums2)]
                    break
            else: # handle add rest of nums1 & break
                if i1 < len(nums1):
                    joint += nums1[i1:len(nums1)]
                break
        return joint

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joint = self._combineSort(nums1, nums2)
        if len(joint) % 2 == 0: # do even
            leftMid = self._getMid(joint)
            rightMid = leftMid + 1
            return (joint[leftMid] + joint[rightMid])/2
        else: # do odd
            return joint[self._getMid(joint)]

class FindMedianSortedArray_SimplyUsingSort:
    def __init__(self) -> None:
        pass

    def _getMid(self, joint):
        return int((len(joint)- 1)/2)

    def _combineSort(self, nums1, nums2):
        joint = nums1 + nums2
        joint.sort()
        return joint

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joint = self._combineSort(nums1, nums2)
        if len(joint) % 2 == 0: # do even
            leftMid = self._getMid(joint)
            rightMid = leftMid + 1
            return (joint[leftMid] + joint[rightMid])/2
        else: # do odd
            return joint[self._getMid(joint)]