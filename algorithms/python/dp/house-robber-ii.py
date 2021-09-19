# https://leetcode.com/problems/house-robber-ii

from typing import List


class Solution:
    def robit(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robit(nums[:len(nums) - 1]), self.robit(nums[1:]))
