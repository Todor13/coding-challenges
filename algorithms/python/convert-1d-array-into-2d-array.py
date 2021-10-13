# https://leetcode.com/problems/convert-1d-array-into-2d-array

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = []
        for i in range(len(original) // n):
            res.append(original[i * n: i * n + n])

        return res
