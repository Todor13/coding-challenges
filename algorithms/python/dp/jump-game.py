# https://leetcode.com/problems/jump-game

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mstep = nums[0]
        for i in range(1, len(nums)):
            if mstep >= i:
                mstep = max(mstep, nums[i] + i)
            else:
                return False

        return mstep >= len(nums) - 1
