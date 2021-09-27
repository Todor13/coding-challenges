# https://leetcode.com/problems/maximum-sum-circular-subarray

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmin, gmin = 0, float('inf')
        cmax, gmax = 0, float('-inf')

        for e in nums:
            cmax = max(cmax + e, e)
            gmax = max(gmax, cmax)

            cmin = min(cmin + e, e)
            gmin = min(gmin, cmin)

        if gmax < 0:
            return gmax

        return max(gmax, sum(nums) - gmin)
