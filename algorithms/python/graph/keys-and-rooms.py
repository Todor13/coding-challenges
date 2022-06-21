# https://leetcode.com/problems/keys-and-rooms

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        q = [0]
        visited[0] = True

        while q:
            room = q.pop(0)

            for i in rooms[room]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)

        return all(visited)
