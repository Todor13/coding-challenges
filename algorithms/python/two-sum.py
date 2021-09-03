# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[0]: 0}
        for i in range(1, len(nums)):
            if (target - nums[i]) in nums_dict:
                return [nums_dict[target - nums[i]], i]
            nums_dict[nums[i]] = i
        return []
