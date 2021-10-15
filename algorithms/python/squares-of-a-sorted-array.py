# https://leetcode.com/problems/squares-of-a-sorted-array

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        result = []
        negatives = []
        while i < len(A) and A[i] <= 0:
            negatives.append(A[i] * -1)
            i += 1

        while i < len(A) or len(negatives) > 0:
            if len(negatives) > 0:
                n = len(negatives) - 1
                if i < len(A) and A[i] <= negatives[n]:
                    result.append(A[i] * A[i])
                    i += 1
                else:
                    a = negatives.pop(-1)
                    result.append(a * a)
            else:
                result.append(A[i] * A[i])
                i += 1

        return result
