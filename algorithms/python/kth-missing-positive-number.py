# https://leetcode.com/problems/kth-missing-positive-number

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, missing = 0, 0
        while k > 0 and i < len(arr):
            missing += 1
            if arr[i] == missing:
                i += 1
            else:
                k -= 1

        if k == 0:
            return missing
        else:
            return missing + k
