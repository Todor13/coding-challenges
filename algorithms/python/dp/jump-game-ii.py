# https://leetcode.com/problems/jump-game-ii

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        curr, reach, jumps = 0, 0, 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if curr == i:
                jumps += 1
                curr = reach
                reach = 0

        return jumps
