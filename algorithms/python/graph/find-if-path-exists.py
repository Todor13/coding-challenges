# https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = defaultdict(list)
        for edge_pair in edges:
            adj[edge_pair[0]].append(edge_pair[1])
            adj[edge_pair[1]].append(edge_pair[0])

        queue = [start]
        visited = [False] * n
        while queue:
            curr_node = queue.pop(0)
            visited[curr_node] = True
            if curr_node == end:
                return True

            for neighbour in adj[curr_node]:
                if not visited[neighbour]:
                    queue.append(neighbour)

        return False
