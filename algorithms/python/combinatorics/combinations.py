# https://leetcode.com/problems/combinations

from typing import List


class Solution:
    def comb_rec(self, comb: List[List[int]], arr: List[int], start: int, n: int, k: int):
        if len(arr) == k:
            comb.append(arr[:])
            return
        for i in range(start, n + 1):
            arr.append(i)
            self.comb_rec(comb, arr, i + 1, n, k)
            del arr[-1]

    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        self.comb_rec(comb, [], 1, n, k)
        return comb
