# https://leetcode.com/problems/reshape-the-matrix

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        res = []
        flatened = [x for s in mat for x in s]
        for i in range(len(flatened) // c):
            res.append(flatened[i * c: i * c + c])

        return res
