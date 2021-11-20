# https://leetcode.com/problems/search-a-2d-matrix-ii

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        cols, rows = len(matrix[0]), len(matrix)
        c, r = 0, 0
        while r < rows:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target > matrix[r][c - 1]:
                r += 1
            elif matrix[r][c] < target:
                if c + 1 < cols:
                    c += 1
                else:
                    r += 1
            elif matrix[r][c] > target:
                if c - 1 >= 0:
                    c -= 1
                else:
                    return False

        return False
