# https://leetcode.com/problems/number-of-provinces/
from typing import List


class Solution:
    def findCircleRec(self, isConnected: List[List[int]], node: int, visited: List[bool]):
        if not visited[node]:
            visited[node] = True
            for n_idx, is_con in enumerate(isConnected[node]):
                if is_con and not visited[n_idx]:
                    self.findCircleRec(isConnected, n_idx, visited)

    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        n = len(is_connected)
        n_provinces = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                n_provinces += 1
                self.findCircleRec(is_connected, i, visited)
        return n_provinces
