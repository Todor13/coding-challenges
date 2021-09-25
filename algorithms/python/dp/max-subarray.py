# https://leetcode.com/problems/maximum-subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [nums[0]] * len(nums)
        m = nums[0]
        for i in range(1, len(nums)):
            arr[i] = max(nums[i], nums[i] + arr[i - 1])
            m = max(m, arr[i])

        return m
