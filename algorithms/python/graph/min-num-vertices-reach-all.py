# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        out, in_ = set([x[0] for x in edges]), set([x[1] for x in edges])
        return list(out.difference(in_))
