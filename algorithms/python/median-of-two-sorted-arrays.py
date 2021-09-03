# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = []
        j, k = 0, 0
        while j < len(nums1) and k < len(nums2):
            if nums1[j] < nums2[k]:
                array.append(nums1[j])
                j += 1
            else:
                array.append(nums2[k])
                k += 1

        while j < len(nums1):
            array.append(nums1[j])
            j += 1

        while k < len(nums2):
            array.append(nums2[k])
            k += 1

        if len(array) % 2 == 0:
            return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
        else:
            return array[len(array) // 2]
