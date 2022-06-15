# https://leetcode.com/problems/all-paths-from-source-to-target

from typing import List


class Solution:
    def allPathsSourceTargetRec(self, graph, node, paths, track):
        track.append(node)
        if node == len(graph) - 1:
            paths.append(track.copy())
        else:
            for neigh in graph[node]:
                self.allPathsSourceTargetRec(graph, neigh, paths, track)
        track.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, track = [], []
        self.allPathsSourceTargetRec(graph, 0, paths, track)
        return paths
