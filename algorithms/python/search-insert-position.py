# https://leetcode.com/problems/search-insert-position

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)

        l, r = 0, len(nums)
        m = l + (r - l) // 2
        while l < r:
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m
            else:
                return m

            m = l + (r - l) // 2

        return m
