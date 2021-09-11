# https://leetcode.com/problems/majority-element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        idx, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[idx]:
                count += 1
            else:
                count -= 1

            if count < 0:
                idx = i
                count = 1

        return nums[idx]
