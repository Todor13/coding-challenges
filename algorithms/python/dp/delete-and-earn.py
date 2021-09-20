# https://leetcode.com/problems/delete-and-earn

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])

    def deleteAndEarn(self, nums: List[int]) -> int:
        m = 0
        for num in nums:
            m = max(m, num)
        arr = [0] * (m + 1)
        for i in range(len(nums)):
            arr[nums[i]] += 1
        for i in range(len(arr)):
            arr[i] = arr[i] * i

        return self.rob(arr)
