# https://leetcode.com/problems/maximum-product-subarray

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref, suf = [0] * len(nums), [0] * len(nums)
        pm, sm = nums[0], nums[-1]

        pref[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != 0:
                pref[i] = pref[i - 1] * nums[i] if pref[i - 1] != 0 else nums[i]
            pm = max(pm, pref[i])

        suf[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != 0:
                suf[i] = suf[i + 1] * nums[i] if suf[i + 1] != 0 else nums[i]
            sm = max(sm, suf[i])

        return max(pm, sm)
